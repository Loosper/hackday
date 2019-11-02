import random
import re

import constants as const
import comms


def make_id(bits):
    return random.getrandbits(bits).to_bytes(bits // 8, 'big')


class DHT:
    def __init__(self):
        self.key_len = const.KEY_LEN
        self.node_id = make_id(self.key_len)
        self.node_table = [[] for _ in range(self.key_len)]
        self.add_node(self.node_id, const.IP, const.PORT)
        # print(self.node_id)

    def __repr__(self):
        rep = []
        for index, bucket in enumerate(self.node_table):
            if bucket:
                rep.append(f'{index}: {bucket}')

        return '\n'.join(rep)

    @staticmethod
    def _bit_equal(b1, b2, i):
        byte_i = (i // 8)
        byte1 = b1[byte_i]
        byte2 = b2[byte_i]

        # couting starts from the front
        mask = (0xF0 >> (i % 8))
        return (byte1 & mask) == (byte2 & mask)

    def _get_bucket(self, id):
        assert type(id) is bytes
        assert len(id) == (self.key_len // 8)

        for i in range(self.key_len):
            if not self._bit_equal(self.node_id, id, i):
                return i
        return const.KEY_LEN - 1


    def add_node(self, new_id, ip, port):
        # assert port >= 0
        # assert port < 2 ** 16
        assert re.match(r'\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}', ip)

        self.node_table[self._get_bucket(new_id)].\
            append((new_id, ip, port))

    def find_node(self, new_id):
        bucket_id = self._get_bucket(new_id)

        # check if it's there
        for node in self.node_table[bucket_id]:
            if node[0] == new_id:
                return node

        # return the top n otherwise
        return self.node_table[bucket_id][0: const.N]

    def remove_node(self, id):
        bucket_id = self._get_bucket(id)
        # warning: inefficient
        for i, node in enumerate(self.node_table[bucket_id]):
            if node[0] == id:
                self.node_table[bucket_id].pop(i)


table = DHT()

if __name__ == '__main__':
    table.add_node(b'\xff', '127.0.0.1', 44)
    print(table)
