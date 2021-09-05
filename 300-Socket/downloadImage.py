import socket
import time

HOST = "data.pr4e.org"
PORT = 80

# https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png

tSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("www.stanford.edu", 80)
tSock.connect((HOST, PORT))
tSock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count =0
picture = b""

while True:
    data = tSock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture+ data


tSock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

picture = picture[pos+4:]
fhandle = open("standford.jpg", "wb")
fhandle.write(picture)
fhandle.close()