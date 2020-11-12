# -*- coding=utf-8 -*-
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9988))
sk.listen()

# The server side can communicate with multiple clients
while True:
    conn,addr = sk.accept()
    # After a successful connection, information can be passed multiple times.
    while True:
        try:
            recv_data = int(conn.recv(1024).decode('utf-8'))
            print(recv_data)
            if recv_data % 2 == 0:
                conn.send("This number is even.".encode('utf-8'))
            else:
                conn.send("This number is odd.".encode('utf-8'))
        except:
            print("Error input.")
            conn.send("Illegal input.Please re-enter the integer.".encode('utf-8'))
            continue
    # Wave to one client and disconnect
    conn.close()

sk.close()
