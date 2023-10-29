import eel
from client import Client


client = Client('127.0.0.1', 1240)


@eel.expose
def get_processes():
    return client.request_ps()


@eel.expose()
def request_kill_process(pid):
    return client.request_kill_ps(pid)


eel.init('client/web')
eel.start('index.html', size=(850, 400), port=0)
