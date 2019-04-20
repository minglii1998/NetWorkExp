from socket import *
 
HOST = "localhost"
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
 
sockCli = socket(AF_INET, SOCK_DGRAM)
 
while True:
        data = raw_input(">")
        if not data:
                break
        sockCli.sendto(data, ADDR)
        data, addr = sockCli.recvfrom(BUFSIZE)
        if not data:
                break
        print data
 
 

