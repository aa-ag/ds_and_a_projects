############------------ IMPORTS ------------############
import heapq as hq
import collections as c


############------------ FUNCTIONS ------------############
def huffman_encoding(data):

    frequencies = c.Counter(data)

    heap = [[value, [key, ""]] for key, value in frequencies.items()]
    hq.heapify(heap)

    while len(heap) > 1:
        left = hq.heappop(heap)
        right = hq.heappop(heap)

        for pair in left[1:]:
            pair[1] = '0' + pair[1]

        for pair in right[1:]:
            pair[1] = '1' + pair[1]

        hq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    encoded = sorted(hq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    print(''.join([e[1] for e in encoded]))

    return heap


huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")


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
