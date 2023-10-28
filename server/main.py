import threading
from time import sleep
from datetime import datetime

from conn_handler import conn_handler
from server import Server


# open sockets
server = Server('', 1240)
server.listen_conns(5)

print(f'\033[92mlistening for connections...\033[00m')

# wait for connection
while True:
    sleep(0.5)
    try:
        client, addr = server.accept_conn()
        print(f'\033[96m{client} connected at {datetime.now()}\033[00m')
        threading.Thread(target=conn_handler, args=(client, )).start()
    except:
        print(f'\033[91m =*= fatal error, shutting down =*= \033[00m')
        client.close()
