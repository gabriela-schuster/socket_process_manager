import socket


class Server:
    clients = []

    def __init__(self, addr, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((addr, port))
        self.server = server


    def listen_conns(self, max_conns):
        self.server.listen(max_conns)


    def accept_conn(self):
        client, addr = self.server.accept()
        Server.clients.append(client)
        return client, addr