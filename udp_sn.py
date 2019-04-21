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
 
sockSrv = socket(AF_INET, SOCK_DGRAM)
sockSrv.bind(ADDR)

user1 = "2160500040"
user2 = "2160500038"
needUname = "Please enter your user name!"
unameWrong = "You enter a wrong user!"
needPw = "Please enter your password!"
pwWrong = "You enter a wrong password!"
PW = "jsj623840"
connSucc = "Connect sucessfully! We have 2 files, enter file1.docx or file2.docx to get it."
wantStop = "Quit"
rece = "received:"
f1Name = "file1.docx"
f2Name = "file2.docx"
 
while True:
		data, addr = sockSrv.recvfrom(BUFSIZE)
		print ('...connected from:',addr)
		while True:
				data, addr = sockSrv.recvfrom(BUFSIZE)
				print(data)
				if ((data.decode('utf-8') == user1 )or(data.decode('utf-8') == user2)):
					sockSrv.sendto(needPw.encode('utf-8'),addr)
					while True:
						data, addr = sockSrv.recvfrom(BUFSIZE)
						if (data.decode('utf-8') == PW):
							sockSrv.sendto(connSucc.encode('utf-8'),addr)
							while True:
								data, addr = sockSrv.recvfrom(BUFSIZE)
								if (data.decode('utf-8') == wantStop):
									break
								elif (data.decode('utf-8') == f1Name):
                                                                        count=0
                                                                        f=open('file1.docx','rb')
                                                                        while True:
                                                                            if count == 0:
                                                                                print ("Are You Ready?")
                                                                            data = f.read(BUFSIZE)
                                                                            if str(data)!="b''":
                                                                                sockSrv.sendto(data,addr)
                                                                            else:
                                                                                sockSrv.sendto('end'.encode('utf-8'),addr) #此处文件结束
                                                                                break

                                                                            #data,addr = sockSrv.recvfrom(BUFSIZE)
                                                                            count+=1
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
									sockSrv.sendto(head_info_len,addr)
									sockSrv.sendto(head_info.encode('utf-8'),addr)
									with open (filemsg,'rb') as f:
										data = f.read()
										sockSrv.sendall(data,addr)
									print('Sended Successfully!')
								else:
									print(data)
									sockSrv.sendto(rece.encode('utf-8'),addr)
						elif (data.decode('utf-8') == wantStop):
							break
						else :
							sockSrv.sendto(pwWrong.encode('utf-8'),addr)
				elif (data.decode('utf-8') == wantStop):
					break
				else :
					sockSrv.sendto(unameWrong.encode('utf-8'),addr)
		sockSrv.close()
 
sockSrv.close()
