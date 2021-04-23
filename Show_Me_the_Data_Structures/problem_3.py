############------------ IMPORTS ------------############
import sys
import collections as c
import heapq as hq


############------------ HELPER CODE ------------############
class Node:
    def __init__(self, character, frequency, left_child, right_child):
        self.character = character
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child


class Heap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def push(self, priority, item):
        self.heap.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return hq.heappop(self.heap)[1]


############------------ FUNCTIONS ------------############


def huffman_encoding(data):
    pass


def huffman_decoding(data, tree):
    pass


############------------ DRIVER CODE ------------############
h = Heap()

h.push(1, "first value here")
h.push(2, "second value here")
print(h.size())  # 2

h.push(3, "third value here")
h.push(4, "fourth value here")

print(h.size())  # 4


# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     generate_priority_queue(a_great_sentence)

# print("The size of the data is: {}\n".format(
#     sys.getsizeof(a_great_sentence)))
# print("The content of the data is: {}\n".format(a_great_sentence))

# encoded_data, tree = huffman_encoding(a_great_sentence)

# print("The size of the encoded data is: {}\n".format(
#     sys.getsizeof(int(encoded_data, base=2))))
# print("The content of the encoded data is: {}\n".format(encoded_data))

# decoded_data = huffman_decoding(encoded_data, tree)

# print("The size of the decoded data is: {}\n".format(
#     sys.getsizeof(decoded_data)))
# print("The content of the encoded data is: {}\n".format(decoded_data))
