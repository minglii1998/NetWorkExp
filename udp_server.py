from socket import *
from time import ctime
 
HOST = ""
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
rece = "received!"
 
sockSrv = socket(AF_INET, SOCK_DGRAM)
sockSrv.bind(ADDR)
 
while True:
        data, addr = sockSrv.recvfrom(BUFSIZE)
        print ("receive %s from %s" % (data, addr))
        sockSrv.sendto(rece.encode('utf-8'), addr)
 
 
sockSrv.close
