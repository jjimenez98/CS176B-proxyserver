import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ("Socket Created")
port=2059
s.bind((socket.gethostname(),port))
print ("Socket binded to %s" %(port))
s.listen(5)
print ("Socket is listenting")
while True:
  networksocket, address = s.accept()
  print ("Got connection from", address)
  networksocket.send(b"Thank you for connecting to server")
  time.sleep(0.5)
  t=time.time()
  print ("server time %s" %(t))
  networksocket.send(bytes(str(t),"utf-8"))
  networksocket.close()
