import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  #There are strings in Python which are unicode and we have to send them as UTF8
mysock.send(cmd)

while True:
    data = mysock.recv(512) #receive up to 512 character
    if len(data) < 1:
        break
    print(data.decode(),end='') #Change it to internal format from UTF8

mysock.close()