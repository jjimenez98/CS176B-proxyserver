import socket
import time
import random
import sys
from tkinter import *
from _thread import *

#tkinter implementation

#theLabel = Label(root, text="This is too easy")
#theLabel.pack()
#root.mainloop()





HEADERSIZE = 10
PROXY_PORT = 9001
# DEST_PORT = 8020
DEST_PORT=sys.argv[1]
header= HEADERSIZE + len(str(DEST_PORT))

#from RTT code
current_sim_time=0
sim_time_at_sync=0
current_sys_time=0
sys_time_at_sync=0
delta=10
t=time.time()
p=(t-0.5)/t

while True:
    t1=time.time()
    print (time.time())                                 #prints the time of the OS
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                 #connects to the proxy server
    s.bind((socket.gethostbyname(""),2021))
    s.connect((socket.gethostbyname(""),PROXY_PORT))
    msg = s.recv(1024)
    print(msg)                                                                          # receive messge from the proxy "Welcome to the Network"
    # info = "This is some message destined to some port"
    info = sys.argv[2]                             # message sent to the server
    info = f'{len(info) + len(str(DEST_PORT)):<{HEADERSIZE}}' + str(DEST_PORT) + info   # adds the PORT number with the message
    print(info)
    s.send(bytes(info,"utf-8"))                                                         # sends message to proxy server

    msg = s.recv(1024)                                                                  # receives the time of the network
    if(msg == b'Message Blocked'):
        break

    # process of calculating the RTT
    tutc=float(msg)
    print("this is tutc %s" %(msg))
    t2=time.time()


    round= tutc - t1
    New_time= t2 + (round/2)
    print ("This is the RTT time: ")
    print (New_time);
    print ("\n")
    sync_every=delta/(2*p)
    time.sleep(sync_every)

    s.close()
