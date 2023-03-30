#!/bin/python3

import socket

(HOST,PORT) = ('127.0.0.1', 4567)

sock = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)

socket.listen()
