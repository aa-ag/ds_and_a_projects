############------------ IMPORTS ------------############
import sys
import collections
import heapq


############------------ FUNCTIONS ------------############
def count_character_frequency(input_string):
    return collections.Counter(input_string.replace(' ', ''))


def huffman_encoding(input_string):

    character_frequency = count_character_frequency(input_string)

    heap = [[weight, [symbol, '']]
            for symbol, weight in character_frequency.items()]

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for value in left[1:]:
            value[1] = '0' + value[1]

        for value in right[1:]:
            value[1] = '1' + value[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    tree = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    return ''.join([i[1] for i in tree]), tree


# def huffman_decoding(data, tree):
#     pass


############------------ DRIVER CODE ------------############
if __name__ == "__main__":

    input_string = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(input_string)))
    print("The content of the data is: {}\n".format(input_string))

    encoded_data, tree = huffman_encoding(input_string)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print("The size of the decoded data is: {}\n".format(
    #     sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))
