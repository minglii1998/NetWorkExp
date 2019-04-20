from socket import *
 
HOST = "localhost"
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
wantStop = "Quit"

sockCli = socket(AF_INET, SOCK_STREAM)
sockCli.connect(ADDR)
 
while True:
        data = input(">")
        if (data == wantStop):
                break
        sockCli.send(data.encode('utf-8'))
        data = sockCli.recv(BUFSIZE)
        if not data:
                break
        print (data)
 
sockCli.close()
