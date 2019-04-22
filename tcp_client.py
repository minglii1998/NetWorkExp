from socket import *
import struct
import json
import os
import sys
import time
 
HOST=input("请输入Server IP地址：")
#HOST = "localhost"
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)
wantStop = "Quit"
f1Name = "file1.docx"
f2Name = "file2.docx"

sockCli = socket(AF_INET, SOCK_STREAM)
sockCli.connect(ADDR)
 
while True:
		#data = sockCli.recv(BUFSIZE)
		#print(data)
		data = input(">")
		if (data == wantStop):
			break
		#sockCli.send(data.encode('utf-8'))
		#data = sockCli.recv(BUFSIZE)
		if (data == 'file1.docx' or data == 'file2.docx'):
			sockCli.send(data.encode('utf-8'))
			time.sleep(0.1)
			head_struct = sockCli.recv(4)
			print ()
			if head_struct:
				print('Waiting for file1!')
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
						print("File transmitted!")
						f.close()
		if (data != "Transmit mode!"):
			sockCli.send(data.encode('utf-8'))
			time.sleep(0.1)
			data = sockCli.recv(BUFSIZE)
			print (data)
 
sockCli.close()
