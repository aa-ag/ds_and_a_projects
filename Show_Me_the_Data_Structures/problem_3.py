############------------ IMPORTS ------------############
import heapq
import collections

############------------ FUNCTIONS ------------############


from heapq import heappush, heappop, heapify
from collections import defaultdict


def encode(data):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in data.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


s = "AAAAAAABBBCCCCCCCDDEEEEEE"

data = collections.Counter(s)

huff = encode(data)
print("Symbol\tWeight\tHuffman Code")
for p in huff:
    print("%s\t%s\t%s" % (p[0], data[p[0]], p[1]))


# def huffman_decoding(data, tree):
#     pass


############------------ DRIVER CODE ------------############
# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print("The size of the data is: {}\n".format(
#         sys.getsizeof(a_great_sentence)))
#     print("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print("The size of the encoded data is: {}\n".format(
#         sys.getsizeof(int(encoded_data, base=2))))
#     print("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print("The size of the decoded data is: {}\n".format(
#         sys.getsizeof(decoded_data)))
#     print("The content of the encoded data is: {}\n".format(decoded_data))
