#!/usr/bin/env python3

import sys
import socket

clientSocket = socket.socket()
host = '192.168.56.5'
port = 8888

print("Connecting.....")

try:
    clientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

msg = clientSocket.recv(1024)
print(msg.decode('utf-8'))
cmsg = "Client 1 has been connected!"
clientSocket.send(cmsg.encode('utf-8'))

while True:

    print("\nMathematical Function")
    print("\nBelow are the options for each function.")
    print("1 - Logarithmic (log)")
    print("2 - Square Root (sqrt)")
    print("3 - Exponential (exp)")
    print("q - Exit")
    option = input('Your Option?:  ')

    if option == '1' or option == '2' or option == '3':
        value = input("Enter a value: ")
        option = option + ":" + value
        clientSocket.send(str.encode(option))

    elif option == 'q':
        print("Exiting system......")
        clientSocket.send(str.encode(option))
        sys.exit()

    else:
        print("Input Error!")
        sys.exit()

    msg = clientSocket.recv(1024)
    print(msg.decode("utf-8"))

clientSocket.close()