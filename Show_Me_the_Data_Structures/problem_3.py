############------------ IMPORTS ------------############
import heapq
import collections

############------------ FUNCTIONS ------------############


def huffman_encoding(data):

    heap = [[v, [k, ""]] for k, v in data.items()]

    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)

        for pair in high[1:]:
            pair[1] = '0' + pair[1]

        for pair in high[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda j: (len(j[-1]), j))


s = "AAAAAAABBBCCCCCCCDDEEEEEE"
character_frequency = collections.Counter(s)
huff = huffman_encoding(character_frequency)

for p in huff:
    print("%s\t%s\t%s" % (p[0], character_frequency[p[0]], p[1]))

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
