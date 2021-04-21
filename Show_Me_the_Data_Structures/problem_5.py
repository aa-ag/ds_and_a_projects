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

    def __init__(self, timestamp, data, previous_hash, next=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "Encoding this!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


first_blockchain = BlockChain()
first_blockchain.head = Block(datetime.now(), 'abcdefg', None)

print(first_blockchain)
