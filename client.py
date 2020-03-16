import socket
import time
import random
import sys
from tkinter import *
from _thread import *


def run():
    HEADERSIZE = 10
    PROXY_PORT = 9001
    messageinput = message_entry.get()

    DEST_PORT = int(port_entry.get())
    CLIENT_PORT = int(port1_entry.get())

    header= HEADERSIZE + len(str(DEST_PORT))

    #from RTT code
    current_sim_time=0
    sim_time_at_sync=0
    current_sys_time=0
    sys_time_at_sync=0
    delta=10
    t=time.time()
    p=(t-0.5)/t

    COUNTER = 0
    RTT_AVERAGE = 0
    NumTests = int(number_entry.get())

    while True:
        t1=time.time()
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                 #connects to the proxy server
        s.bind((socket.gethostbyname(""),CLIENT_PORT))
        s.connect((socket.gethostbyname(""),PROXY_PORT))
        msg = s.recv(1024)
        print(msg)                                                                          # receive messge from the proxy "Welcome to the Network"

        info = messageinput                                                                 # message sent to the server
        info = f'{len(info) + len(str(DEST_PORT)):<{HEADERSIZE}}' + str(DEST_PORT) + info   # adds the PORT number with the message
        #print(info)
        s.send(bytes(info,"utf-8"))                                                         # sends message to proxy server

        msg = s.recv(1024)                                                                  # receives the time of the network
        if(msg == b'Message Blocked'):
            break

            # process of calculating the RTT
        tutc=float(msg)
        #print("this is tutc %s" %(msg))
        t2=time.time()


        round= tutc - t1
        RTT = (round*1000) - 500
        New_time= t2 + (round/2)
        print ("This is the RTT time: ")
        print (RTT);
        print ("\n")
        COUNTER = COUNTER + 1
        CLIENT_PORT = CLIENT_PORT + COUNTER
        RTT_AVERAGE = RTT_AVERAGE+RTT
        if COUNTER == NumTests:
            RTT_AVERAGE = RTT_AVERAGE/NumTests
            print("This is the average RTT of the # of test runs")
            print(RTT_AVERAGE)
            break
        time.sleep(1)
        s.close()


#tkinter implementation
root = Tk()
message = Label(root, text = "message")
Port = Label(root, text = "Destination PORT #")
Port_1 = Label(root, text = "Client PORT #")
button_1 = Button(root,text = "Submit",command = run)
Numberoftests = Label(root, text = "Number of Tests")

message_entry = Entry(root)
port_entry = Entry(root)
port1_entry = Entry(root)
number_entry = Entry(root)

message.grid(row=0)
Port.grid(row=1)
Port_1.grid(row=2)
Numberoftests.grid(row=3)


message_entry.grid(row=0, column=1)
port_entry.grid(row=1, column=1)
port1_entry.grid(row=2, column=1)
number_entry.grid(row=3,column=1)
button_1.grid(row=4)
root.mainloop()
