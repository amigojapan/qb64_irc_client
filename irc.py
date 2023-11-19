import socket
import select
import atexit, termios
import sys, os
import time
import fcntl
import errno
import random

# Generate a random integer between a specified range
random_number = random.randint(1, 100)
server  = "irc.libera.chat"
nick    = "shortestPyIRC" + str(random_number)
channel = "##anime"

old_settings=None

def init_any_key():
   global old_settings
   old_settings = termios.tcgetattr(sys.stdin)
   new_settings = termios.tcgetattr(sys.stdin)
   new_settings[3] = new_settings[3] & ~(termios.ECHO | termios.ICANON) # lflags
   new_settings[6][termios.VMIN] = 0  # cc
   new_settings[6][termios.VTIME] = 0 # cc
   termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)


@atexit.register
def term_any_key():
   global old_settings
   if old_settings:
      termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def any_key():
   ch = os.read(sys.stdin.fileno(), 1)
   if len(ch)>0:
       return ch

init_any_key()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, 6667))
fcntl.fcntl(client, fcntl.F_SETFL, os.O_NONBLOCK)

user_input = ""
print("waiting 15 seconds for connect...\r\n server:"+server+" nick:"+nick+" channel:"+channel)
time.sleep(15) #wait enough till logon

line = f"nick {nick}\r\nuser a a a a\r\n"
print (line +" nick and user ***")
client.send(line.encode())
time.sleep(2)

line = f"join {channel}\r\n"
print (line +" joining channel ***")
client.send(line.encode())
time.sleep(2)
cc=0
# ... (previous code)

buff = ""
while True:
    try:
        buff = client.recv(4096)
        if buff:
            print(buff.decode(), end="")
        if buff.startswith("PING".encode()):  # handle PING
            s = buff[4:]
            #line = f"PONG{s}\r\n"
            line = f"PONG\r\n"
            print("pong reached", line)
            client.send(line.encode())
            time.sleep(2)

    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            # No data available from the socket, handle input
            time.sleep(0.05)  # 50ms delay (20 checks per second)
            key = any_key()
            if key is not None:
                # Handle user input here
                if key == b'\x7f':
                    # Backspace pressed
                    user_input = user_input[:-1]
                    print("")
                    print(user_input)
                elif key == b'\n':
                    # Enter pressed
                    line = f"privmsg {channel} : {user_input}\r\n"
                    client.send(line.encode())
                    print("sending:", line)
                    time.sleep(2)
                    user_input = ""
                    print("")
                else:
                    # Alphanumeric key pressed
                    user_input += key.decode()
                    sys.stdout.write(key.decode())
                    sys.stdout.flush()
        else:
            # A "real" error occurred
            print(e)
            sys.exit(1)
