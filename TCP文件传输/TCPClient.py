# -*- coding=utf-8 -*-
import socket
import os
import time

filename = input('please enter the filename you want to send:\n')
filesize = str(os.path.getsize(filename))
fname1, fname2 = os.path.split(filename)
client_addr = ('127.0.0.1',9999)
f = open(filename,'rb')
# count = 0
# flag = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Establish a connection:
s.connect(('127.0.0.1', 9999))
while True:
    # if count == 0:
    s.send(filesize.encode())
    start = time.time()
    current_start = time.time()
    s.recv(1024)
    s.send(fname2.encode())
    for line in f:
        s.send(line)
        # Statistics the current system running time
        current_end = time.time()
        # If 1s is run, the current time of
        # printing is used as one of the coefficients of the end-to-end delay
        if current_end-current_start >1:
            print(current_end)
            current_start = time.time()
    s.send(b'end')
    break

s.close
end = time.time()
print('cost ' + str(round(end - start, 6)) + 's')
