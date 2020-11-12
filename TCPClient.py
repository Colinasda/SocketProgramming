# -*- coding=utf-8 -*-
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9988))

while True:
    # The client prompts for digital information.
    msg_send_to_server = input("Client:Please enter the integer: ").encode('utf-8')
    # Transmit the received information to the server side for processing.
    sk.send(msg_send_to_server)
    # The client receives the information passed by the server and prints it.
    msg_recv_from_server = sk.recv(1024).decode('utf-8')
    print(msg_recv_from_server)

sk.close()
