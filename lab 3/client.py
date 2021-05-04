
from rpc import *
import sys

port = '127.0.0.1'
host = 9999

# robj = rpccopy.rpc(port,host)
robj = rpc_connect(port,host) # server host and server port
print("client initialted\n")
while True:
    x=input("1 for sensor 1 data\n2 for sensor 2 data\nq to quit\n")
    if x=="1":
        t=robj.sensor1("get reading")
        print(t)
    elif x=="2":
        t=robj.sensor2("get reading")
        print(t)
    elif x=='q':
        sys.exit("Quitting!!!!")
    else:
        print("Function Does not Exist!")

print()
robj.close_conn()
