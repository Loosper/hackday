import random
import re


KEY_LEN = 8

def make_id(bits):
    return random.getrandbits(bits).to_bytes(bits // 8, 'big')


class DHT:
    def __init__(self):
        self.key_len = KEY_LEN
        self.node_id = make_id(self.key_len)
        self.node_table = [[] for _ in range(self.key_len)]
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
        assert len(id) == self.key_len // 8

        for i in range(self.key_len):
            if not self._bit_equal(self.node_id, id, i):
                return i


    def add_node(self, new_id, ip, port):
        assert port >= 0
        assert port < 2 ** 16
        assert re.match(r'\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}', ip)

        self.node_table[self._get_bucket(new_id)].\
            append((new_id, ip, port))

    def find_node(self, new_id, n):
        bucket_id = self._get_bucket(new_id)

        # check if it's there
        for node in self.node_table[bucket_id]:
            if node[0] == new_id:
                return node

        # return the top n otherwise
        return self.node_table[bucket_id][0: n]

    def remove_node(self, id):
        bucket_id = self._get_bucket()
        # warning: inefficient
        for i, node in enumerate(self.node_table[bucket_id]):
            if node[0] == id:
                self.node_table[bucket_id].pop(i)



if __name__ == '__main__':
    table = DHT()
    table.add_node(b'\xff', '127.0.0.1', 44)
    print(table)
