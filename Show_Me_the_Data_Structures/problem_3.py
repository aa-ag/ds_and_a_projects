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

    def push(self, item):
        hq.heappush(self.heap, item)

    def pop(self):
        return hq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def __getitem__(self, item):
        return self.heap[item]

    def __len__(self):
        return len(self.heap)


############------------ FUNCTIONS ------------############
def count_character_frequency(data):
    return c.Counter(data.replace(' ', ''))


def huffman_encoding(data):
    character_frequency = count_character_frequency(data)
    '''
    Counter({'h': 2, 'e': 2, 'i': 2, 'r': 2, 'd': 2, 
    'T': 1, 'b': 1, 's': 1, 't': 1, 'w': 1, 'o': 1})
    '''

    heap = Heap()

    for value, frequency in sorted(character_frequency.items(), key=lambda x: x[1]):
        heap.push([frequency, value])

    left = heap.pop()
    right = heap.pop()

    print(left, right)


def huffman_decoding(data, tree):
    pass


############------------ DRIVER CODE ------------############
# h = Heap()

# h.push([1, "first value here"])
# h.push([2, "second value here"])
# h.push([3, "third value here"])
# h.push([4, "fourth value here"])

# print(h.pop())

# for i in h:
#     print(i)

'''
[1, 'first value here']
[2, 'second value here']
[3, 'third value here']
[4, 'fourth value here']
'''

if __name__ == "__main__":
    # codes = {}

    a_great_sentence = "The bird is the word"

    huffman_encoding(a_great_sentence)

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
