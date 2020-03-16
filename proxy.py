import socket
import time
from _thread import *
import threading
import random

#List of Ports the proxy will filter
ListofPorts = [1000,8000]
#List of words the proxy will filter
ListofWords = ["Beyond","detail","guiding","deliverable",
"understand","potentially","risk","report","requirements","number","examples","reports",
"Second","serves","problem","end","evaluation","detailed","system","themes","solving","expand","task",
"prespective","software","protocols","operation","demonstrate","concepts","cheating","advance","routers",
"delay","compression","intercept","security","major","report","company","code","performance","parallel","examples","message"]

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

header= HEADERSIZE + port_size                                                      #this is because of the port being part of the header
                                                                                    #this is agreed upon before hand, if the port was a longer number, then this size
                                                                                    #would increase


#x PORT to be filtered if in the list
def filter_port(x):
    print("Applying filtering port function")
    result = False
    for i in ListofPorts:
        if i == x:
            result = True;
    return result

#a list of words
#b original message

def filter_words(a,b):
    print("Applying filtering word function")
    space = ""
    originalword = b
    for i in ListofWords:

        for x in range(len(i)):
            space = space + " "

        originalword = originalword.replace(i,space)
        space = ""
    return originalword


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
            #print(body)

            newmsg = filter_words(ListofWords,body)
            #newmsg = body

            DEST_PORT = int(full_msg[HEADERSIZE:header])                            #get the DEST PORT from the message

            filter = filter_port(SERVERPORT)
            if(filter == True):
                print("Filtered packet")
                clientsocket.send(b'Message Blocked')
                break

            delay1=random.uniform(0,1)                                              #add random delay to mimic the network
            time.sleep(delay1/1000)                                                 #sleep by the delay initialized
            server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                # start the process of send xto the server
            server.connect((socket.gethostbyname(""),DEST_PORT))                    #connects to the server
            info=newmsg                                                               #Gets the message sent from the client
            info = f'{len(info):<{HEADERSIZE}}' + info
            server.send(bytes(info,"utf-8"))                                        #send the message
            msg = server.recv(1024)                                                 #reeives the time of OS fron the server

            delay2=random.uniform(0,1)                                              #add dealy to network
            time.sleep(delay2/1000)                                                 #sleep by the random delay
            clientsocket.send(msg)                                                  #send time from server -> proxy server
            print ("\n")
            server.close()
            break

    clientsocket.close()


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostbyname(""),PROXY_PORT))                                       # binds to PORT
print ("socket is binded")
s.listen(5)                                                                         # listens to the client
print ("socket is listening")


while True:                                                                         #keeps connection comstantly
    clientsocket, address = s.accept()                                              #accepts the client
    print("Got connection from", address)
    start_new_thread(clientthread, (clientsocket,address))                          # implement the multiple thread method
    #thread = clientthread(clientsocket,address)
    #thread.start()

s.close()
