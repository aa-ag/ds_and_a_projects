############------------ IMPORTS ------------############
import sys
import collections


############------------ FUNCTIONS ------------############
def generate_pseudo_heap(s):

    character_frequency = collections.Counter(s)

    characters = character_frequency.keys()

    pseudo_heap = []

    for character in characters:
        pseudo_heap.append((character_frequency[character], character))

    pseudo_heap.sort()

    return pseudo_heap


def build_tree(pseudo_heap):
    while len(pseudo_heap) > 1:
        two_lower_values = tuple(pseudo_heap[0:2])

        rest_of_pseudo_heap = pseudo_heap[2:]

        merge = two_lower_values[0][0] + two_lower_values[1][0]

        pseudo_heap = rest_of_pseudo_heap + [(merge, two_lower_values)]

        pseudo_heap = sorted(pseudo_heap, key=lambda x: x[0])

    return pseudo_heap[0]


def trim_tree(tree):
    leaf = tree[1]

    if type(leaf) == str:
        return leaf
    else:
        return (trim_tree(leaf[0]), trim_tree(leaf[1]))


def encode(node, pat=''):
    global codes

    if type(node) == str:
        codes[node] = pat
    else:
        encode(node[0], pat + '0')
        encode(node[1], pat + '1')


def huffman_encoding(s):
    global codes

    output = ''

    for character in s:
        output += codes[character]

    return output


def huffman_decoding(tree, s):
    output = ''

    leaf = tree

    for bit in s:
        if bit == '0':
            leaf = leaf[0]
        else:
            leaf = leaf[1]
        if type(leaf) == str:
            output += leaf
            leaf = tree

    return output


##############------ DRIVER CODE -----------############
codes = {}

# s = 'aaabccdeeeeeffg'
s = 'The bird is the word'

pseudo_heap = generate_pseudo_heap(s)

tree = build_tree(pseudo_heap)

trim = trim_tree(tree)

encode(trim)

encoded_data = huffman_encoding(s)
print(encoded_data)

print(huffman_decoding(trim, encoded_data))

# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print()

#     print("The size of the data is: {}\n".format(
#         sys.getsizeof(a_great_sentence)))
#     print("The content of the data is: {}".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print("The size of the encoded data is: {}\n".format(
#         sys.getsizeof(int(encoded_data, base=2))))
#     print("The content of the encoded data is: {}".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print("The size of the decoded data is: {}\n".format(
#         sys.getsizeof(decoded_data)))
#     print("The content of the encoded data is: {}".format(decoded_data))
