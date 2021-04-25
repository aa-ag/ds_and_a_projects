############------------ IMPORTS ------------############
import collections


############------------ FUNCTIONS ------------############
def count_character_frequency(s):
    character_frequency = collections.Counter(s)

    return character_frequency


def sort_character_frequency(character_frequency):
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


def encode(node, branch=''):
    global codes

    if type(node) == str:
        codes[node] = branch
    else:
        encode(node[0], branch + '0')
        encode(node[1], branch + '1')


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

s = 'aaabccdeeeeeffg'

character_frequency_table = count_character_frequency(s)

pseudo_heap = sort_character_frequency(character_frequency_table)

tree = build_tree(pseudo_heap)

trim = trim_tree(tree)

encode(trim)

encoded_data = huffman_encoding(s)
print(encoded_data)

print(huffman_decoding(trim, encoded_data))
