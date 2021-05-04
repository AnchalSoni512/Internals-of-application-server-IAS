import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8000        # The port used by the server
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))

url = input("enter url in desired format\neg. GET site1/filename.extension\n\n")
#get url in desired format
# extension = url[-3:]
split_url = url.split('/')
filename = split_url[1]
extension = split_url[1].split(".")
extension = extension[1]
# print(extension)
# print (filename)
url2 ="GET /"+url[4:]+" HTTP/1.1"

mysock.send(url2.encode())
data = mysock.recv(1024)
header,content = data.split(b'\n\n',1)
# print(header.decode())
check = str(header.decode())
if "NOT" in check:
    # print("this file does not exist")
    mysock.close()
    sys.exit("This file does not exist !!!")

with open(filename, "wb") as F:
    while content:
        F.write(content)
        content = mysock.recv(1024)
    F.close()
    print(filename+" has been downloaded on your system!")
    # print(data.decode(),end='')
mysock.close()