import socket
import time
HEADERSIZE = 10
PROXY_PORT = 9000
DEST_PORT = 8020
header= HEADERSIZE + len(str(DEST_PORT))

# print(header)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),PROXY_PORT))
info = "This is some message destined to some port"
info = f'{len(info) + len(str(DEST_PORT)):<{HEADERSIZE}}' + str(DEST_PORT) + info
print(info)
s.send(bytes(info,"utf-8"))
s.close()
# while True:
#     full_msg=''
#     new_msg=True
#     while True:
#         msg = s.recv(16)
#         if new_msg:
#             print(f"new message length: {msg[:HEADERSIZE]}")
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False
#         full_msg += msg.decode("utf-8")
#         if len(full_msg) - HEADERSIZE == msglen:
#             print("full msg recvd")
#             print(full_msg)
#             print(full_msg[header:])
#             new_msg = True
#             full_msg == ''
#             port = full_msg[HEADERSIZE:header]
#             print (port)

            # info = "This is some message destined to some port"
            # info = f'{len(msg) + len(str(DEST_PORT)):<{HEADERSIZE}}' + str(DEST_PORT) + info
            # s.send(bytes(info,"utf-8"))
            # time.sleep(2)

# print("\n")
# info = "This is some message destined to some port"
# info = f'{len(info) + len(str(DEST_PORT)):<{HEADERSIZE}}' + str(DEST_PORT) + info
# print(info)
# s.send(bytes(info,"utf-8"))
# print(msg)
