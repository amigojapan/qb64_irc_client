# qb64_irc_client

linux binary available! just download it and run it!
mac x86 and windows binaries provided by phigan (who compiled on macOS　10.15.7 and test on 12.7.1) much appreciation!

windows binary is x86_64(64 bit windows only) it won"t run on 32 bit computers do to restrictions of QB64.

download QB64 and run it and change the nickname and channel and network and port, see the following instructions:

you will need qb64 to modify the code and run it with your own nick and channel 
https://qb64.com/

you will just need to mess with 

server$ = "irc.libera.chat"

nick$ = "quickbasicIRC" REM  you can get rid of the random number if you choose your won nickname here

channel$ = "##anime"

client = _OpenClient("TCP/IP:6667:" + server$)

install python3

to run the python program, just type

python3 irc.py 



install lua

sudo apt-get install lua

sudo apt-get install luarocks

sudo luarocks install luasocket

sudo apt-get install lua-posix

to run the python program, just type

lua irc.lua 
