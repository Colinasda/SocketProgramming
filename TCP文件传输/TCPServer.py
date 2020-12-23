# -*- coding=utf-8 -*-
import socket
import time

count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

while True:
    sock, addr = s.accept()
    print('Accept new connection from %s:%s...' % addr)
    if count == 0:
        data1 = sock.recv(1024)
        print(str(data1))
        file_total_size = int(data1.decode())
        received_size = 0
        sock.send('received'.encode())
        data = sock.recv(1024)
        filepath = str(data.decode())
        f = open(filepath, 'wb')
        start = time.time()
    while received_size < file_total_size:
        data = sock.recv(1024)
        f.write(data)
        received_size += len(data)
        # Count the system time after each iteration
        end = time.time()
        # If 1s is run,
        # print the current time and the current cumulative number of transfers
        if end - start > 1:
            print(end)
            print('Accept ', received_size, ' B')
            start = time.time()
    data = sock.recv(1024)
    if data == b'end':
        break
print(end-start)

f.close()
s.close()
