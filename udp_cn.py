from socket import *
import struct
import json
import os
import sys
import time
 
HOST = "localhost"
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
wantStop = "Quit"
f1Name = "file1.docx"
f2Name = "file2.docx"
init = "Connected!"
sockCli = socket(AF_INET, SOCK_DGRAM)
sockCli.connect(ADDR)
sockCli.sendto(init.encode('utf-8'),ADDR)

while True:
		data = input(">")
		if (data == wantStop):
			break
		if (data == f1Name):
                    sockCli.sendto(data.encode('utf-8'),addr)
                    count=0
                    f=open('newfile1.docx','wb')
                    while True:
                        if count == 0:
                            data='Yes,I\'m Ready'
                            #sockCli.sendto(data.encode('utf-8'),addr)
                        data,addr = sockCli.recvfrom(BUFSIZE)
                        if str(data)!="b'end'":
                            f.write(data)
                        else:
                            break
                        count+=1
                        #client.sendto('ok'.encode('utf-8'),addr)
                        #print("File1 transmitted!")
                    f.close()
		if (data == f2Name):
			sockCli.sendto(data.encode('utf-8'),addr)
			time.sleep(0.1)
			head_struct = sockCli.recv(4)
			print ()
			if head_struct:
				print('Waiting for file2!')
				head_len = struct.unpack('i', head_struct)[0]
				data = sockCli.recv(head_len)
				head_dir = json.loads(data.decode('utf-8'))
				data = "Transmit mode!"
				filesize_b = head_dir['filesize_bytes']
				file_name = head_dir['file_name']
				recv_len = 0
				recv_mesg = b''
				f = open(file_name, 'wb')
				while recv_len < filesize_b:
					if filesize_b - recv_len > BUFSIZE:
						recv_mesg = sockCli.recv(BUFSIZE)
						f.write(recv_mesg)
						recv_len += len(recv_mesg)
					else:
						recv_mesg = sockCli.recv(filesize_b - recv_len)
						recv_len += len(recv_mesg)
						f.write(recv_mesg)
						print("File2 transmitted!")
		if (data != "Transmit mode!"):
			sockCli.sendto(data.encode('utf-8'),ADDR)
			time.sleep(0.1)
			data, addr = sockCli.recvfrom(BUFSIZE)
			print (data)
 
sockCli.close()
