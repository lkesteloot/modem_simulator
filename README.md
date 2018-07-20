This program displays text in a terminal at modem speeds. It can connect to the
[fozztexx BBS](http://bbs.fozztexx.com/) or display a local text file. Early
1980s speeds were 300 and 1200 baud, so you can try that if you want to see
what signing into a BBS was like at the time:

    % python modem_simulator.py 300 fidonet.txt
    Welcome to FidoNet!
                        __
                       /  \
                      /|oo \
                     (_|  /_)
                      _`@/_ \    _
                     |     | \   \\
                     | (*) |  \   ))
        ______       |__U__| /  \//
       / FIDO \       _//|| _\   /
      (________)     (_/(_|(____/
     (c) John Madil

    Username: 

Omit the filename to connect to the fozztexx BBS:

    % python modem_simulator.py 300
    Welcome to the *NEW* Level 29 BBS!
    916 965 1701 - bbs.fozztexx.com

                  __
      ___________/__\___________
     /   _  _  -__ -   ___  -   \
     \__________________________/
                 |  |
                 |  |
            _____|  |______
        ___|     |  |      |___
       |   |     |  |      |   |
    ___|___|____/____\_____|___|___
                            __   __
    |     __        __  |  /  \ /  \
    |    /__\ |  | /__\ |   __/ \__/
    |___ \__   \/  \__  |  /___   /

    The official BBS of
    RetroBattlestations.com


    Enter your username or NEW or VISITOR
    User:

I used a 300 baud modem for a year, then saw a friend's 1200 baud modem
signing into a BBS. My subjective experience was that the page loaded
near-instantaneously. In reality it probably took 3 to 5 seconds.

# License

Copyright 2018 Lawrence Kesteloot

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
