from client import Client


client = Client('127.0.0.1', 1238)
while True:
    print(client.request_ps())
    pid = int(input('PID to terminate: '))