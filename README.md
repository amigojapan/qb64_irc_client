# qb64_irc_client

linux binary available! just download it and run it!
mac x86 binary provided by phigan(I have not tested it myself(I dont have a mac anymore))

download QB64 and run it there if you run windows and mac
(for now, I will eventually build a windows version)

you will need qb64 to modify the code and run it with your own nick and channel 
https://qb64.com/

you will just need to mess with 

server$ = "irc.libera.chat"

nick$ = "quickbasicIRC" REM  you can get rid of the random number if you choose your won nickname here

channel$ = "##anime"

client = _OpenClient("TCP/IP:6667:" + server$)

to run the python program, just type
python3 irc.py 
