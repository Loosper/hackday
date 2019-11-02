import re
import sys
import socket
import hashlib
import argparse

import dht
import constants as const
import comms


def validate_ip(ip):
    if re.match(r'\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}', ip):
        return ip
    else:
        raise argparse.ArgumentTypeError('not a valid ip')

parser = argparse.ArgumentParser(
    description='Secure & distributed file storage'
)
parser.add_argument('entry', type=validate_ip)
parser.add_argument('port', type=int)
parser.add_argument(
    '-u', help='upload a file to the network', dest='upload')
parser.add_argument(
    '-d', help='download a file to the network', dest='download')
parser.add_argument(
    '-l', help='run a node in the network', dest='listen')


if __name__ == "__main__":
    args = parser.parse_args()
    ip = '127.0.0.1'

    server = comms.Server()
    server.start()
    try:
        print(comms.find_id(args.entry, args.port))

        if args.listen:
            pass
        elif args.upload:
            id = hashlib.sha1(args.upload.encode('utf-8')).digest()[:(const.KEY_LEN // 8)]
            peers = comms.find_peer(id)
            peers.sort(key=lambda x: dht.table._get_bucket(x[0]))
            # print(peers)
            # while True:
            #     comms.send('hello', ip, port)
            #     input()
    except ConnectionRefusedError:
        print('couln\'t connect to anyone')
        print('youre might be the first on the network')
        pass


    try:
        server.join()
    except KeyboardInterrupt:
        server.close()

