from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

def sub(a,b):
    return int(a)-int(b)
def add1(a,b):
    return int(a)+int(b)
def add2(a,b,c):
    return int(a)+int(b)+int(c)

class my_FTP_handler(FTPHandler):
    def on_file_sent(self,file):
        print("sent!")
        os.remove(file)

    def on_file_received(self,file):
        print("received!")
        f = open(file,'r')
        read = f.readline()
        q = read.split(' ')
        len_arg = len(q[1:])
        if q[0] == 'sub':
            out = sub(q[1],q[2])
        elif q[0] == 'add' and len_arg == 2:
            out = add1(q[1],q[2])
        elif q[0] == 'add' and len_arg == 3:
            out = add2(q[1],q[2],q[3])
        else:
            out = "function does not exist!"
        os.remove(file)
        f = open(file,'w')
        f.write(str(out))
        f.close()


authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", ".", perm="elradfmw")
authorizer.add_anonymous(".", perm="elradfmw")

handler = my_FTP_handler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()
