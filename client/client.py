import socket


class Client:
    clients = []

    def __init__(self, addr, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((addr, port))
        self.client = client


    def request_ps(self):
        pss = []
        self.client.sendall('ps'.encode())
        while True:
            ps = self.client.recv(2048).decode()
            if 'endps' in ps:
                print('got all processes from server')
                return pss
            pss.append(ps)
