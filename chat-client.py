#!/bin/python3
import socket
import threading

(HOST,PORT) = ('10.35.4.61', 9001)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST,PORT))

print('Connected')

def get():
    while True:
        received_data = sock.recv(1024)
        print(received_data)

threading.Thread(target=get).start()

while True:
    data = input()
    sock.sendall(bytes(data, 'utf-8'))

