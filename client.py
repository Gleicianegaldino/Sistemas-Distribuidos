#!/bin/python3

import socket

(HOST,PORT) = ('127.0.0.1', 9001)

sock = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)

sock.connect((HOST,PORT))

print('Connected')

print('Type something: ')

data = input()
sock.sendall(bytes(data, 'utf-8'))
data = sock.recv(1024)
print(data)