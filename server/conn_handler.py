import os
from scanner import Scanner


scanner = Scanner()


def conn_handler(client):
    while True:
        data = client.recv(2048).decode()
        replier(client, data)


# replies the client with the desired action / data
def replier(client, cmd):
    if cmd == 'ps':
        print(f'client {client} requested processes')
        pss = scanner.get_processes()
        for ps in pss:
            client.sendall(ps.encode())
        client.sendall('endps'.encode())
        print(f'sent all processes to {client}')
    else:
        client.sendall('invalid operation'.encode())

