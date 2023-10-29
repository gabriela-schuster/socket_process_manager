from scanner import Scanner
from time import sleep


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
            sleep(0.0005)
        client.sendall('endps'.encode())
        print(f'sent all processes to {client}')

    elif 'terminate' in cmd:
        pid = cmd.replace('terminate ', '')
        print(f'\033[93m{client} requested to terminate process {pid}\033[00m')
        try:
            # os.popen('').read()
            client.sendall('success'.encode())
        except:
            client.sendall('error'.encode())

    else:
        client.sendall('invalid operation'.encode())

