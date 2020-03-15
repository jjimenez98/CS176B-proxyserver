import socket
import time
from _thread import *
import random


ListofPorts = [2000,8020,2020]
ListofWords = ["this","port","to"]

#x PORT to be filtered if in the list

def filter_port(x):
    result = False
    for i in ListofPorts:
        if i == x:
            result = True;
    return result

#a list of words
#b original message

def filter_words(a,b):
    space = ""
    originalword = b
    for i in ListofWords:

        for x in range(len(i)):
            space = space + " "

        originalword = originalword.replace(i,space)
        space = ""
    return originalword




#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#r=socket.gethostname()
#print(r)
print ("Network Created")
port=2001
server_port=2052

HEADERSIZE = 10
PROXY_PORT=9001
port_size = 4
temp = 8000
count=0
innerloop=0
got_Port=False
#DEST_PORT=8020
header= HEADERSIZE + port_size                                                      #this is because of the port being part of the header
                                                                                    #this is agreed upon before hand, if the port was a longer number, then this size
                                                                                    #would increase

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostbyname(""),PROXY_PORT))                                       # binds to PORT
print ("socket is binded")
s.listen(5)                                                                         # listens to the client
print ("socket is listening")

def clientthread(clientsocket,address):
    SERVERPORT = address[1]
    clientsocket.send(b'Welcome to the Network')
    full_msg=''
    new_msg=True
    while True:
        temp = clientsocket.recv(16)                                                # to receive the header and the port number
        if new_msg:
            msglen = int(temp[:HEADERSIZE])
            new_msg=False
        full_msg += temp.decode("utf-8")
        if len(full_msg) - HEADERSIZE == msglen:
            body=full_msg[header:]
            print(body)

            newmsg = filter_words(ListofWords,body)

            DEST_PORT = int(full_msg[HEADERSIZE:header])                            #get the DEST PORT from the message

            filter = filter_port(SERVERPORT)
            if(filter == True):
                clientsocket.send(b'Message Blocked')
                break

            delay1=random.uniform(0,1)                                              #add random delay to mimic the network
            print (" delay1: %s" %delay1)
            time.sleep(delay1/1000) #delay                                          #sleep by the delay initialized
            server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                # start the process of send xto the server
            server.connect((socket.gethostbyname(""),DEST_PORT))                    #connects to the server
            info=newmsg                                                               #Gets the message sent from the client
            info = f'{len(info):<{HEADERSIZE}}' + info
            server.send(bytes(info,"utf-8"))                                        #send the message
            msg = server.recv(1024)                                                 #reeives the time of OS fron the server
            print(msg)
            print (float(msg));                      # prints in time in localtime
            print ("time UTC received")
            delay2=random.uniform(0,1)                                              #add dealy to network
            print ("delay2: %s" %(delay2))
            time.sleep(delay2/1000)                                                 #sleep by the random delay
            clientsocket.send(msg)                                                  #send time from server -> proxy server
            print ("\n")
            server.close()
            break

    clientsocket.close()

while True:                                                                         #keeps connection comstantly
    clientsocket, address = s.accept()                                              #accepts the client
    print("Got connection from", address)
    start_new_thread(clientthread, (clientsocket,address))                                 # implement the multiple thread method

s.close()
