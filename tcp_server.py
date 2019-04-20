from socket import *
from time import ctime
 
HOST = ""
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
 
sockSrv = socket(AF_INET, SOCK_STREAM)
sockSrv.bind(ADDR)
sockSrv.listen(5)
user1 = "2160500040"
user2 = "2160500039"
needUname = "Please enter your user name!"
unameWrong = "You enter a wrong user!"
needPw = "Please enter your password!"
pwWrong = "You enter a wrong password!"
PW = "jsj623940"
connSucc = "Connect sucessfully! You can begin transmit data!"
wantStop = "Quit"
rece = "received:"
 
while True:
		sockCli,addr = sockSrv.accept()
		print ('...connected from:',addr)	
		sockCli.send(needUname.encode('utf-8'))
		while True:
				data = sockCli.recv(BUFSIZE)
				if ((data.decode('utf-8') == user1 )or(data.decode('utf-8') == user2)):
					sockCli.send(needPw.encode('utf-8'))
					while True:
						data = sockCli.recv(BUFSIZE)
						if (data.decode('utf-8') == PW):
							sockCli.send(connSucc.encode('utf-8'))
							while True:
								data = sockCli.recv(BUFSIZE)
								if (data.decode('utf-8') == wantStop):
									break
								else:
									print(data)
									sockCli.send(rece.encode('utf-8'))
									sockCli.send(data)
						elif (data.decode('utf-8') == wantStop):
							break
						else :
							sockCli.send(pwWrong.encode('utf-8'))
				elif (data.decode('utf-8') == wantStop):
					break
				else :
					sockCli.send(unameWrong.encode('utf-8'))
						
						#if not data:
						#		break
						#print (data);
						#sockCli.send(data)
						
		sockCli.close()
 
sockSrv.close()
