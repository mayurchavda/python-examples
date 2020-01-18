import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(err)

port = 80

try:
    host_ip = socket.gethostname()
    print(host_ip)
    host_ip = socket.gethostbyname("https://www.google.co.in")
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()

s.connect((host_ip,port))

print("The socket has successfully connected to google on port == %s"%(host_ip))


