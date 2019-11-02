import socket
import time
from threading import Thread


class Server(Thread):
    def __init__(self, port=2000, *args, **kwargs):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind(('0.0.0.0', port))
        self.soc.listen(1)

        super().__init__(*args, **kwargs)

    def run(self):
        for msg in self.listen():
            print(msg)

    def listen(self):
        while True:
            con, addr = self.soc.accept()
            print("Connected to {}".format(con))

            message = b''
            while True:
                data = con.recv(1024)
                if not data:
                    break
                message += data

            yield message

def send(msg, recepient, port):
    # assert type(msg) is bytes

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    encoded_msg = msg.encode("utf-8")
    soc.connect((recepient, port,))

    sent = 0
    while True:
        sent += soc.send(encoded_msg[sent:])

        if sent == 0:
            print('an error occured')
            break

        if sent >= len(encoded_msg):
            break

