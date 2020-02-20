import socket
import time
HEADERSIZE = 10
PROXY_PORT=9000
port_size = 4
temp = 8000
count=0
innerloop=0
got_Port=False
DEST_PORT=0
header= HEADERSIZE + port_size #this is because of the port being part of the header
#this is agreed upon before hand, if the port was a longer number, then this size
#would increase

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),PROXY_PORT))
print ("socket is binded")
s.listen(5)
print ("socket is listening")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    # msg = "Welcome to the server!"
    # msg =f'{len(msg) + port_size:<{HEADERSIZE}}' + str(temp) + msg
    # clientsocket.send(bytes(msg,"utf-8"))
# has served as a server to the client
# now needs to act a client to the destination or 'server'
    full_msg=''
    new_msg=True
    while True:
        # innerloop+=1
        # print (f"innerloop = {innerloop}")
        temp = clientsocket.recv(16) # to receive the header and the port number
        if new_msg:
            print(f"new message length: {temp[:HEADERSIZE]}")
            msglen = int(temp[:HEADERSIZE])
            new_msg=False
        full_msg += temp.decode("utf-8")
        if len(full_msg) - HEADERSIZE == msglen:
            print(full_msg)
            body=full_msg[header:]
            print(body)
            DEST_PORT = int(full_msg[HEADERSIZE:header])
            print(DEST_PORT)
            # clientsocket.close()

            server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((socket.gethostname(),DEST_PORT))
            info=body
            info = f'{len(info):<{HEADERSIZE}}' + info
            print(info)
            server.send(bytes(info,"utf-8"))
            server.close()
            break
    clientsocket.close()
