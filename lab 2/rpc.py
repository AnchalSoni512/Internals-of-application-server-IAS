import socket,ast

class rpc_connect:
    def __init__(self,HOST,PORT):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((HOST,PORT))
        data = s.recv(1024).decode('utf-8')
        data_dict = ast.literal_eval(data)
        # print(data_dict)
        for fun_name in data_dict:
            def func_description(fun_name):#function fun_name-> add,sub
                fn_name = fun_name
                def __call__(self, *args):
                    if(len(args) == len(data_dict[fun_name])):
                        f_dict = {fn_name:list(args)} # {'add':[2,3]}
                        # print(f_dict)
                        fname = str(f_dict)
                        s.sendall(fname.encode())
                        res = s.recv(1024).decode()
                    else:
                        print("incorrect args in " + fn_name)
                        exit()
                    return res
                setattr(rpc_connect,fun_name,__call__)
            func_description(fun_name)
    
    def close_conn(self):
        x = {"close":[0]}
        x = str(x)
        s.sendall(x.encode())
	