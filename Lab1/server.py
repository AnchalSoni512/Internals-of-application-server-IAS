import socket
import mimetypes
import os

def handle_request(request):

    url = request.split('\n')
    # print(url[0])
    filename = url[0].split()[1]
    print(filename[1:]+' requested by the client\n')
    content_type = mimetypes.guess_type(filename[1:])[0]

    try:
        fin = open(filename[1:],"rb")
        content = fin.read()
        file_stats = os.stat(filename[1:])
        content_lenght = file_stats.st_size
        fin.close()
        
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Type:" + content_type +"; charset=utf-8\r\n" +str(content_lenght)+"\r\n" +"Content-Disposition: attachment;\r\n"
        header += "\n"

    except FileNotFoundError:
        header = "HTTP/1.0 404 NOT FOUND\r"
        header += "\n\n"
        content = 'HTTP/1.0 404 NOT FOUND\n'
        content = content.encode()
        # return content.encode()
    # return response
    return header.encode()+content

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print('\nServer running and Listening on port %s ...' % SERVER_PORT)
    print('\nAccess http://localhost:8000\n')

    while True:    
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        response = handle_request(request)    
        client_connection.sendall(response)
        client_connection.close()

except KeyboardInterrupt :
    print("\nShutting down...\n")
except Exception as exc :
    print("Error:")
    print(exc)

    server_socket.close()
