import socket
import time
import random

#Pythom time method time() returns the time as a floating point number expressed in seconds.

current_sim_time=0
sim_time_at_sync=0
current_sys_time=0
sys_time_at_sync=0
delta=10
t=time.time()
p=(t-0.5)/t
while True:
    t1=time.time()

    print ("this is T1 %s" %(t1))
    print (time.asctime( time.localtime(time.time()) ))
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=2001
    s.connect((socket.gethostbyname(""),port))
    msg = s.recv(1024)
    print (msg)
    t=s.recv(1024)
    t_sec=time.time()
    print ("this is t2 %s" %(t_sec))
    tutc=float(t)
    print("this is tutc %s" %(t))
    current_sys_time=time.time()
    print (current_sys_time)
    print ("\n")
    sign=random.randint(1,3)
    if(sign==1):
        current_sim_time=sim_time_at_sync + (current_sys_time-sys_time_at_sync)*(1+p)
    else:
        current_sim_time=sim_time_at_sync + (current_sys_time-sys_time_at_sync)*(1-p)
    sys_time_at_sync=current_sys_time
    sim_time_at_sync=current_sim_time
    round=(current_sys_time-current_sim_time)/2
    New_time=tutc+round
    print ("This is the new time %s" %(New_time))
    sync_every=delta/(2*p)
    time.sleep(sync_every)



# full_msg = ''
# while True:
#     msg = s.recv(8)
#     if len(msg) <=0:
#         break
#     full_msg += msg.decoder("utf-8")
# print(full_msg)
