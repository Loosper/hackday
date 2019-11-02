import json
import socket

import constants as const
from threading import Thread

import dht

def receive(con):
    message = b''
    while True:
        data = con.recv(1024)
        if not data:
            break
        message += data
    print(message)
    return message


def sendall(msg, con):
    if type(msg) is not bytes:
        msg = msg.encode("utf-8")

    sent = 0
    while True:
        sent += con.send(msg[sent:])
        if sent == 0:
            print('an error occured')
            break

        if sent >= len(msg):
            break


class Server(Thread):
    def __init__(self, port=const.PORT, *args, **kwargs):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind(('0.0.0.0', port))
        self.soc.listen(1)

        super().__init__(*args, **kwargs)
        self.daemon = True

    def close(self):
        self.soc.close()

    def run(self):
        for msg, con in self.listen():
            msg = json.loads(msg)
            if msg['msg'] == 'FIND_NODE':
                print(bytearray.fromhex(msg['target']))
                node = dht.table.find_node(bytes(bytearray.fromhex(msg['target'])))
                sendall(node, con)
            elif msg['msg'] == 'GET_ID':
                sendall(str(dht.table.node_id), con)
            con.close()

    def listen(self):
        while True:
            con, addr = self.soc.accept()
            print("Connected to {}".format(con))

            message = receive(con)

            yield (message, con,)
            con.close()


def send(msg, recepient, port):
    # assert type(msg) is bytes

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((recepient, port,))
    sendall(msg, soc)
    # tell the other side i'm finished?
    soc.shutdown(socket.SHUT_WR)
    # get the resonse
    resp = receive(soc)
    soc.close()

    return resp

def find_id(ip, port):
    id = send(json.dumps({
        'msg': 'GET_ID'
    }), ip, port)


    dht.table.add_node(id, ip, port)
    return id


def find_peer(id, closeness=0):
    candidates = []
    result = []
    closer = False

    for node in dht.table.find_node(id):
        response = send(json.dumps({
            'msg': 'FIND_NODE',
            'target': id.hex()
        }), node[1], node[2])
        candidates.extend(json.loads(response))

    for node in candidates:
        new_close = dht.table._get_bucket()
        if new_close > closeness:
            result.append(find_peer(node[0], new_close))
            closer = True

    if closer is False:
        return candidates
    else:
        return result
