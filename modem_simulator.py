
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

# Eight bits for the data, one start bit, one stop bit.
BITS_PER_BYTE = 10

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: file.txt baud\n")
        sys.exit(1)

    # Get the arguments.
    pathname = sys.argv[1]
    baud = int(sys.argv[2])

    # Load the file.
    try:
        contents = open(pathname).read()
    except IOError, e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)

    # Record when this started. We base everything on that so that
    # there's no accumulated error.
    start_time = time.time()

    for i in range(len(contents)):
        now = time.time()

        # Compare where we are to where we should be.
        real_elapsed = now - start_time
        expected_elapsed = float(i*BITS_PER_BYTE)/baud
        how_early = max(expected_elapsed - real_elapsed, 0)

        # Sleep enough to slow down.
        time.sleep(how_early)

        # Write the next character.
        sys.stdout.write(contents[i])
        sys.stdout.flush()

if __name__ == "__main__":
    main()
