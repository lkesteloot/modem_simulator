
# Displays a file in the terminal at modem speeds.

# Copyright 2018 Lawrence Kesteloot
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import sys
import socket
import select

# Eight bits for the data, one start bit, one stop bit.
BITS_PER_BYTE = 10

# Address of fozztexx BBS.
FUZZ_FQDN = "bbs.fozztexx.com"

# Write "text" at "baud" speed.
def write_slowly(text, baud):
    # Record when this started. We base everything on that so that
    # there's no accumulated error.
    start_time = time.time()

    for i in range(len(text)):
        now = time.time()

        # Compare where we are to where we should be.
        real_elapsed = now - start_time
        expected_elapsed = float(i*BITS_PER_BYTE)/baud
        how_early = max(expected_elapsed - real_elapsed, 0)

        # Sleep enough to slow down.
        time.sleep(how_early)

        # Write the next character.
        sys.stdout.write(text[i])
        sys.stdout.flush()

# Connect to fozztexx BBS.
def fozztexx(baud):
    import telnetlib
    import termios
    import tty

    # Open a Telnet connection.
    t = telnetlib.Telnet(FUZZ_FQDN)
    ts = t.get_socket()

    # Put stdin into raw mode so we can get one character at a time and
    # not echo.
    stdin_fd = sys.stdin.fileno()
    old_stdin_tty = termios.tcgetattr(stdin_fd)
    try:
        tty.setraw(stdin_fd)

        while True:
            # Wait to see whether we first get Telnet data or stdin data.
            read_sockets, write_sockets, error_sockets = select.select([ts, sys.stdin], [], [])

            for s in read_sockets:
                if s == ts:
                    # Read a bunch from Telnet.
                    try:
                        x = t.read_eager()
                    except EOFError:
                        sys.stdout.write("\r\n*** Connection closed by remote host ***\r\n")
                        return
                    except socket.error, e:
                        sys.stdout.write("\r\n" + str(e) + "\r\n")
                        return

                    write_slowly(x, baud)
                elif s == sys.stdin:
                    ch = sys.stdin.read(1)

                    # Check for Ctrl-C.
                    if ord(ch) == 3:
                        sys.stdout.write("\r\n^C\r\n")
                        t.close()
                        return
                    t.write(ch)
    finally:
        # Restore terminal.
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_stdin_tty)

def usage():
    sys.stderr.write("Usage: modem_simulator.py baud [file.txt]\n")
    sys.exit(1)

def main():
    # Parse command-line arguments.
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        usage()

    baud = int(sys.argv[1])

    if len(sys.argv) == 3:
        pathname = sys.argv[2]

        # Load the file.
        try:
            contents = open(pathname).read()
        except IOError, e:
            sys.stderr.write(str(e) + "\n")
            sys.exit(1)

        write_slowly(contents, baud)
    else:
        fozztexx(baud)

if __name__ == "__main__":
    main()

