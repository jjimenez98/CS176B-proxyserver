import socket
import time
HEADERSIZE = 10
Server_Port=8020
port_size = 4
temp = 8000
header= HEADERSIZE + port_size                                                  #this is because of the port being part of the header
                                                                                #this is agreed upon before hand, if the port was a longer number, then this size
                                                                                #would increase

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)                              #acceots the proxy server
s.bind((socket.gethostbyname(""),Server_Port))                                  #binds to PORT
print ("socket is binded")
s.listen(5)                                                                     #waits for proxy server to send message
print ("socket is listening")

while True:
    clientsocket, address = s.accept()                                          #acceots the proxy server
    print(f"Connection from {address} has been established!")
    full_msg=''
    new_msg=True
    while True:
        msg = clientsocket.recv(16)                                             #accept the message sent from client
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg.decode("utf-8")                                         #get message
        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg == ''
            time.sleep(0.5)                                                     #delay
            t=time.time()                                                       #get time of OS
            print (time.time())
            clientsocket.send(bytes(str(t),"utf-8"))                            #send time of the OS of server
            print ("\n")
            clientsocket.close()
            break
