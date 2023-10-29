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
            scanner.terminate_ps(int(pid))
            client.sendall('success'.encode())
        except Exception as e:
            client.sendall(f'error: {e}'.encode())

    else:
        client.sendall('invalid operation'.encode())

