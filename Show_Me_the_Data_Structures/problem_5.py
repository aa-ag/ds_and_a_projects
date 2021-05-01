############------------ IMPORTS ------------############
import hashlib
from datetime import datetime


############------------ HELPER CODE ------------############
class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def __repr__(self):
        if not self.timestamp or not self.data or not self.hash:
            return 'empty block'
        return self.data

    def calc_hash(self):
        # create a SHA-256 hash object.
        # this allows us to feed this object
        # with bytes-like objects (normally bytes)
        # using the update() method.
        sha = hashlib.sha256()

        # returns a bytes representation of the Unicode string,
        # encoded in the requested encoding.
        hash_string = self.data.encode('utf-8')

        sha.update(hash_string)

        # Return the digest of the data passed
        # to the update() method so far.
        # This is a bytes object of size digest_size
        # which may contain bytes
        # in the whole range from 0 to 255.
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None


# TEST 1
# Trying to create an empty block
def test_case_1():
    empty_blockchain = BlockChain()
    empty_blockchain.head = Block('', '', '')
    return empty_blockchain.head


# TEST 2
# Try to create different blocks with the same timestamp
def test_case_2():
    two_blocks_with_same_timestamp = BlockChain()
    two_blocks_with_same_timestamp.head = Block(
        datetime.now(), '1', None)
    two_blocks_with_same_timestamp.next = Block(
        datetime.now(), '2', None)

    return two_blocks_with_same_timestamp.head.timestamp, two_blocks_with_same_timestamp.next.timestamp

# TEST 3
# first_blockchain = BlockChain()
# first_blockchain.head = Block(datetime.now(), 'abcdefg', None)
# first_blockchain.next = Block(datetime.now(), 'hijklmn', first_blockchain.head)
# first_blockchain.next.next = Block(
#     datetime.now(), 'opqrstu', first_blockchain.next)

# print(first_blockchain.head)  # abcdefg
# print(first_blockchain.head.timestamp)  # 2021-04-20 19:58:26.874650
# print(first_blockchain.head.hash)
# # 7d1a54127b222502f5b79b5fb0803061152a44f92b37e23c6527baf665d4da9a
# print()

# print(first_blockchain.next)  # hijklmn
# print(first_blockchain.next.timestamp)  # 2021-04-20 19:58:26.874718
# print(first_blockchain.next.previous_hash)  # abcdefg
# print(first_blockchain.next.hash)
# # a2cc0056817d002901742f20883fb838f296af3a4fa9dbb6da71b8af69ccd4d5
# print()

# print(first_blockchain.next.next)  # opqrstu
# print(first_blockchain.next.next.timestamp)  # 2021-04-20 19:58:26.874726
# print(first_blockchain.next.next.previous_hash)  # hijklmn
# print(first_blockchain.next.next.hash)
# # 0eb6146ed8b2eff5b1f9ab848b6534d1cab216040f5d729070e6ba0208a6789a


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # print(test_case_1())
    # empty block

    print(test_case_2())
    # (datetime.datetime(2021, 4, 30, 20, 10, 59, 696464), datetime.datetime(2021, 4, 30, 20, 10, 59, 696483))
