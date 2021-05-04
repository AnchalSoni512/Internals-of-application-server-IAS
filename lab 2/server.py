import socket
import os
import ast
# from _thread import *
# import threading

class functions:
	def __init__(self):
		pass
	def add(self,a,b):
		return a+b
	def mul(self,a,b):
		return a*b
	def concat(self,msg):
		msg = msg+msg
		return msg
	def sen(self,s):
		s1 = "hii have a good day "+s
		return s1
	def sen2(self,s):
		return "this is sentence 2 testing with variable: "+s
	def newfunc(self, p):
		return 2**p
	def pratik(self,a,b):
		return a/b
funs_obj = functions()

function_info = {
	'mul':['int','int'],
	'add':['int','int'],
	'concat':['str'],
	'sen':['str'],
	'sen2':['str'],
	'newfunc':['int'],
	'pratik':['int','int'],
}

def handle_request(client_connection, client_address):
	
	function_data_str = str(function_info)
	# print(function_data_str)
	client_connection.send(function_data_str.encode())
    # funs_obj = functions(10,20)
	while True:
		response = client_connection.recv(1024).decode()
		# print("this is the response " + response)
		fun_call = ast.literal_eval(response)
		print("client asked for: "+response)
		fname = list(fun_call.keys())[0]
		# print(fname)
		arguments = fun_call[fname]
		# print(arguments)
		if(fname != 'close'):
			client_connection.send(str(getattr(funs_obj,fname)(*arguments)).encode())
		else:
			client_connection.close()
			break

		# if fname=='add':
		# 	res=funs_obj.add(arguments[0],arguments[1])
		# 	client_connection.send(str(res).encode())
		# elif fname=='mul':
		# 	res = funs_obj.mul(arguments[0],arguments[1])
		# 	client_connection.send(str(res).encode())
		# elif fname=='sen':
		# 	res = funs_obj.sen(arguments[0])
		# 	client_connection.send(str(res).encode())
		# elif fname=='concat':
		# 	res = funs_obj.concat(arguments[0])
		# 	client_connection.send(str(res).encode())
		# else:
		# 	client_connection.close()
		# 	break

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
	server_socket.bind((SERVER_HOST, SERVER_PORT))
	server_socket.listen(5)
	print('\nServer started and Listening on port %s ...' % SERVER_PORT)

	while True:
		client_connection, client_address = server_socket.accept()
		print("connection accepted.listening to this address ",client_address)
		handle_request(client_connection, client_address)    

except KeyboardInterrupt :
    print("\nShutting down...\n")
except Exception as exc :
    print("Error: ", end ='')
    print(exc)

    server_socket.close()
