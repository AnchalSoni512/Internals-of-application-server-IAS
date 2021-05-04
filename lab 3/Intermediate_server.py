import socket
import os
import ast
from _thread import *

request=[]
response=[]
def sensor1(a):
    global request
    global response
    ans=""
    if "get reading" in a:
        request.append('sensor1')
        while len(response)==0:
            pass
        ans=response[0]
        response=response[1:]
    return ans 
def sensor2(a):
    global request
    global response
    ans=""
    if "get reading" in a:
        request.append('sensor2')
        print("in sensor 2", len(request))
        while len(response)==0:
            pass
        ans=response[0]
        response=response[1:]
    return ans 
def RequestFull(clientsocket):
    global request
    global response
    if len(request)==0:
        clientsocket.sendall(b"No Requests Yet!!")
    else:
        x=request[0]
        request=request[1:]
        x=str(x)
        clientsocket.sendall(x.encode())
        ans=clientsocket.recv(5000).decode()
        response.append(ans)

def client_thread_conn(client_connection_socket):
    rd = client_connection_socket.recv(5000).decode()
    rd=eval(rd)
    print(rd)
    fname=""
    ans=""
    for ele in rd.keys():
        fname=ele
    print(fname)
    if fname=="sensor1":
        ans=str(sensor1(rd['sensor1']))
        client_connection_socket.sendall(ans.encode())
    elif fname=="sensor2":
        ans=str(sensor2(rd['sensor2']))
        client_connection_socket.sendall(ans.encode())
    elif fname=="isRequest":
        str(RequestFull(client_connection_socket))
    else:
        ans="Wrong method called! Particular Method not Present at server"
        clientsocket.sendall(ans.encode())



# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999
# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	server_socket.bind((SERVER_HOST, SERVER_PORT))
	server_socket.listen(5)
	print('\nServer started and Listening on port %s ...' % SERVER_PORT)

	while True:
		client_connection_socket, client_address = server_socket.accept()
		# print("connection accepted.listening to this address ",client_address)
		start_new_thread(client_thread_conn,(client_connection_socket,))

except KeyboardInterrupt :
    print("\nShutting down...\n")
except Exception as exc :
    print("Error: ", end ='')
    print(exc)

server_socket.close()

