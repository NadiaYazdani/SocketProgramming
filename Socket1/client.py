import socket

HOST = '127.0.0.1'
s = socket.socket()
s.connect((HOST,12345))
while True:
    str = raw_input("S: ")
    s.send(str.encode());
    if(str == "Bye" or str == "bye"):
        break
    print "N:",s.recv(1024).decode()
s.close()
