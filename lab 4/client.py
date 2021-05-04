from ftplib import FTP
import sys
import os 

def uploadFile():
    ftp = FTP('')
    ftp.connect('localhost',1026)
    ftp.login()
    ftp.cwd('files') #replace with your directory
    # ftp.retrlines('LIST')
    filename = 'testing.txt' #replace with your file in your home folder
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

def downloadFile():
    ftp = FTP('')
    ftp.connect('localhost',1026)
    ftp.login()
    ftp.cwd('.') #replace with your directory
    # ftp.retrlines('LIST')

    filename = 'output.txt' #replace with your file in the directory ('directory_name')
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + '/files/testing.txt', localfile.write, 1024)
    ftp.quit()
    localfile.close()

ip = input()
f = open('testing.txt', 'w')
f.write(ip)
f.close()
# ip = ip.split(' ')
if ip != '':
    uploadFile()
    downloadFile()
    f = open('output.txt','r')
    data = f.readline()
    print(data)
else:
    print("no input received!")
    sys.exit()

os.remove('testing.txt')
os.remove('output.txt')
# os.remove('/files/testing.txt')

# uploadFile()
# downloadFile()