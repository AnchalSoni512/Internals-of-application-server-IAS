import socket,ast
data_dict = {"sensor1":[1],"sensor2":[1]}

class rpc_connect:

    def __init__(self,HOST,PORT):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((HOST,PORT)) # IP = '127.0.0.1'and port = 9999
        for s_name in data_dict:
            self.func_description(s_name) 

    def func_description(self,s_name):
        def __call__(self, *args):
            if(len(args) == len(data_dict[s_name])):
                f_dict = {s_name:list(args)} 
                # print(f_dict)
                fname = str(f_dict)
                s.sendall(fname.encode())
                res = s.recv(1024).decode()
            else:
                print("incorrect args in " + s_name)
                exit()
            return res
        setattr(rpc_connect,s_name,__call__) ## calls __call__ and sets attribute 
   
    
    def close_conn(self):
        x = {"close":[0]}
        x = str(x)
        s.sendall(x.encode())
	