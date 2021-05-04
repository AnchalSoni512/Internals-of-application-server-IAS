import socket
import schedule
import time
def Request():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1',9999)) # connect to intermediate server
        f_d={"isRequest" : 1}
        x=str(f_d)
        s.sendall(x.encode())
        request=s.recv(5000).decode()
        print(request)
        if request!="No Requests Yet!!":
            data=""
            if request=="sensor1":
                with open("sensor1.txt","r") as f:
                    data=f.read()
                with open("sensor1.txt","w") as f:
                    f.write("")
            elif request=="sensor2":
                with open("sensor2.txt","r") as f:
                    data=f.read()
                with open("sensor2.txt","w") as f:
                    f.write("")
            s.sendall(data.encode())

schedule.every(10).seconds.do(Request)

while True:
    schedule.run_pending()