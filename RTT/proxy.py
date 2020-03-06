import socket
import time
from _thread import *
import random
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
r=socket.gethostname()
print(r)
print ("Network Created")
port=2002
server_port=2059
s.bind((socket.gethostname(),port))
print ("Network binded to %s" %(port))
s.listen(5)
print ("Network is listenting")
def clientthread(clientsocket):
    clientsocket.send(b'Welcome to the Network')
    print("Network connected")
    delay1=random.uniform(1,5)
    print (" delay1: %s" %delay1)
    time.sleep(delay1) #delay
    #now network will act as client and get time from server
    n=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    n.connect((socket.gethostname(),server_port))
    msg = n.recv(1024)
    print(msg)
    t=n.recv(1024)
    print ("time UTC received")
    delay2=random.uniform(1,5)
    print ("delay2: %s" %(delay2))
    time.sleep(delay2)
    clientsocket.send(t)
    #t=time.time()
    #clientsocket.send(str(t))

    clientsocket.close()

while True:
  clientsocket, address = s.accept()
  print ("Got connection from", address)
  start_new_thread(clientthread, (clientsocket,))



s.close()
