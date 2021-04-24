############------------ IMPORTS ------------############
import sys
import collections
import heapq


############------------ FUNCTIONS ------------############
def count_character_frequency(input_string):
    return collections.Counter(input_string.replace(' ', ''))


def huffman_encoding(input_string):

    character_frequency = count_character_frequency(input_string)

    heap = [[frequency, [character, '']]
            for character, frequency in character_frequency.items()]

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for i in left[1:]:
            i[1] = '0' + i[1]

        for j in right[1:]:
            j[1] = '1' + j[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    tree = sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[-1]), x))

    '''
    [['d', '001'], ['e', '010'], ['h', '011'], ['i', '100'], ['r', '110'], 
    ['T', '0000'], ['b', '0001'], ['o', '1010'], ['s', '1011'], ['t', '1110'], 
    ['w', '1111']]
    '''
    encoded_data = ''.join([i[1] for i in tree])

    return encoded_data, tree


def huffman_decoding(encoded_data, tree):
    output = ""
    p = tree
    for bit in encoded_data:
        if bit == '0':
            p = p[0]  # go left
        else:
            p = p[1]  # go right

        if type(p) == type(""):
            output += p  # found a character. Add to output
            p = tree  # and restart for next character

    return output


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

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
