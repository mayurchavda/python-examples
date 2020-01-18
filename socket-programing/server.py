import socket

s = socket.socket()
port = 12345

s.bind(('127.0.0.1',port))
s.listen(5)
print("Server is listening on %d"%port)
while(True):
    con, addr = s.accept()
    print("Got connection from {0}".format(addr))
    con.send(b"Thank you for connecting")
    con.close()

