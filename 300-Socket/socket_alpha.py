import socket

tSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("www.stanford.edu", 80)
tSock.connect(addr)

cmd = 'GET https://www.stanford.edu/wp-content/uploads/2021/07/20210527_Stanford_OvalDJI_0037-DG-2048x1108.jpg HTTP/1.1\r\n\r\n'.encode()
tSock.send(cmd)

while True:
    data = tSock.recv(2048)
    if len(data) < 1:
        break
    print(data.decode(), end='')

tSock.close()
