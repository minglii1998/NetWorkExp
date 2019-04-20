from socket import *
from time import ctime
import struct
import json
import os
import sys
 
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
connSucc = "Connect sucessfully! We have 2 files, enter file1.docx or file2.docx to get it."
wantStop = "Quit"
rece = "received:"
f1Name = "file1.docx"
f2Name = "file2.docx"
 
while True:
		sockCli,addr = sockSrv.accept()
		print ('...connected from:',addr)	
		#sockCli.send(needUname.encode('utf-8'))
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
								elif (data.decode('utf-8') == f1Name):
									filemsg = f1Name
									filesize_bytes = os.path.getsize(filemsg)
									file_name = 'new' + f1Name
									dric = {
										'file_name': file_name,
										'filesize_bytes': filesize_bytes,
									}
									head_info = json.dumps(dric)
									head_info_len = struct.pack('i', len(head_info))
									sockCli.send(head_info_len)
									sockCli.send(head_info.encode('utf-8'))
									with open (filemsg,'rb') as f:
										data = f.read()
										sockCli.sendall(data)
									print('Sended Successfully!')
								elif (data.decode('utf-8') == f2Name):
									filemsg = f2Name
									filesize_bytes = os.path.getsize(filemsg)
									file_name = 'new' + f2Name
									dric = {
										'file_name': file_name,
										'filesize_bytes': filesize_bytes,
									}
									head_info = json.dumps(dric)
									head_info_len = struct.pack('i', len(head_info))
									sockCli.send(head_info_len)
									sockCli.send(head_info.encode('utf-8'))
									with open (filemsg,'rb') as f:
										data = f.read()
										sockCli.sendall(data)
									print('Sended Successfully!')
								else:
									print(data)
									sockCli.send(rece.encode('utf-8'))
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
