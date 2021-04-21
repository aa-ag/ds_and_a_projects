'''
A Blockchain is a sequential chain of records, similar to a linked list. 
Each block contains some information and 
how it is connected related to the other blocks in the chain. 
Each block contains a cryptographic hash of the previous block, 
a timestamp, and transaction data. 
For our blockchain we will be using a SHA-256 hash, 
the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and 
hashing to create a blockchain implementation.

We can break the blockchain down into three main parts.

First is the information hash:
'''
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
        return self.data

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "Encoding this!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None


first_blockchain = BlockChain()
first_blockchain.head = Block(datetime.now(), 'abcdefg', None)
first_blockchain.next = Block(datetime.now(), 'hijklmn', first_blockchain.head)
first_blockchain.next.next = Block(
    datetime.now(), 'opqrstu', first_blockchain.next)

print(first_blockchain.head)  # abcdefg
print(first_blockchain.head.timestamp)  # 2021-04-20 19:58:26.874650
print(first_blockchain.head.hash)
# 0a9ced2c3eafd83ef77295dedf997bd475275594eff10ba83e9bedfbc686120b
print()

print(first_blockchain.next)  # hijklmn
print(first_blockchain.next.timestamp)  # 2021-04-20 19:58:26.874718
print(first_blockchain.next.previous_hash)  # abcdefg

print(first_blockchain.next.next)  # opqrstu
print(first_blockchain.next.next.timestamp)  # 2021-04-20 19:58:26.874726
print(first_blockchain.next.next.previous_hash)  # hijklmn
