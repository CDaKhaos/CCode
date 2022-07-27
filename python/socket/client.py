"""
file : client
"""

import socket
import sys

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 5678))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))
    while 1:
        data = input('Please input work: ').encode()
        s.send(data)
        recv_data = s.recv(1024).decode()
        print('aa', recv_data)
        if recv_data == 'exit':
            break;
    s.close()

if __name__ == '__main__':
    socket_client()
