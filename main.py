import re
import sys
import socket
import hashlib
import argparse

import dht
import comms


def validate_ip(ip):
    if re.match(r'\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}', ip):
        return ip
    else:
        raise argparse.ArgumentTypeError('not a valid ip')

parser = argparse.ArgumentParser(
    description='Secure & distributed file storage'
)
parser.add_argument('entry', gltype=validate_ip)
parser.add_argument(
    '-u', help='upload a file to the network', dest='upload')
parser.add_argument(
    '-d', help='download a file to the network', dest='download')
parser.add_argument(
    '-l', help='run a node in the network', dest='listen')




if __name__ == "__main__":
    args = parser.parse_args()
    ip = '127.0.0.1'
    port = 2000

    server = comms.Server(port)
    server.start()

    if args.listen:
        pass
        # while True:
        #     comms.send('hello', ip, port)
        #     input()




    server.join()

