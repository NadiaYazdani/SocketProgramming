import socket

HOST = '127.0.0.1'
s = socket.socket()
port = 12345
s.bind((HOST, port))
s.listen(5)
c, addr = s.accept()
print "Socket Up and running with a connection from",addr
while True:
    rcvdData = c.recv(1024).decode()
    print "S:",rcvdData
    sendData = raw_input("N: ")
    c.send(sendData.encode())
    if(sendData == "Bye" or sendData == "bye"):
        break
c.close()
