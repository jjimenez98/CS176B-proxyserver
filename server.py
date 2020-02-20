import socket

HEADERSIZE = 10
Server_Port=8020
port_size = 4
temp = 8000
header= HEADERSIZE + port_size #this is because of the port being part of the header
#this is agreed upon before hand, if the port was a longer number, then this size
#would increase

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),Server_Port))
print ("socket is binded")
s.listen(5)
print ("socket is listening")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    full_msg=''
    new_msg=True
    while True:
        msg = clientsocket.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg.decode("utf-8")
        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg)
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg == ''
            clientsocket.close()
            break




    # msg = "Welcome to the server!"
    # msg =f'{len(msg) + port_size:<{HEADERSIZE}}' + str(temp) + msg
    # clientsocket.send(bytes(msg,"utf-8"))
