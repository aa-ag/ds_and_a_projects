############------------ IMPORTS ------------############
import sys
import collections


############------------ FUNCTIONS ------------############
def huffman_encoding(s):
    '''
     creates empty string, imports global codes variable,
     iterates through input string `s` and pupolates output
     string with either a 0 or a 1 depending on frequency 
     using global variable `codes` which is itself prepared in 
     function `encode`
    '''
    global codes

    huffman_encoded_output = ''

    for character in s:
        huffman_encoded_output += codes[character]

    return huffman_encoded_output


def huffman_decoding(tree, encoded_data):
    '''
     creates empty string, and using the `tree` created
     in `build_tree()` function, together with ecoded data
     generated in `huffman_encoding`, iterates over tree to 
     find what character corresponds with either a 0 or a 1
    '''
    huffman_decoded_output = ''

    leaf = tree

    for bit in encoded_data:
        if bit == '0':
            leaf = leaf[0]
        else:
            leaf = leaf[1]

        if type(leaf) == str:
            huffman_decoded_output += leaf
            leaf = tree

    return huffman_decoded_output


def generate_pseudo_heap(s):
    '''
     counts frequency of each character in input string `s`
     creates a list of charactes called `characters` and generates
     a pseudo min heap of tuples
    '''
    character_frequency = collections.Counter(s)

    characters = character_frequency.keys()

    pseudo_heap = []

    for character in characters:
        pseudo_heap.append((character_frequency[character], character))

    pseudo_heap.sort()

    return pseudo_heap


def build_tree(pseudo_heap):
    '''
     builds a tree merging two lowest values from pseudo
     min heap created in `generate_pseudo_heap` and creating
     branches and parent nodes
    '''
    while len(pseudo_heap) > 1:
        two_lower_values = tuple(pseudo_heap[0:2])

        rest_of_pseudo_heap = pseudo_heap[2:]

        merge = two_lower_values[0][0] + two_lower_values[1][0]

        pseudo_heap = rest_of_pseudo_heap + [(merge, two_lower_values)]

        pseudo_heap = sorted(pseudo_heap, key=lambda x: x[0])

    tree = pseudo_heap[0]

    '''
    this is what `tree` looks like:

    (20, ((8, ((4, ((2, 'h'), (2, 'i'))), (4, ((2, 'r'), (2, ((1, 'T'), \
    (1, 'b'))))))), (12, ((4, ((2, ((1, 'o'), (1, 's'))), (2, ((1, 't'), \
    (1, 'w'))))), (8, ((4, ' '), (4, ((2, 'd'), (2, 'e')))))))))
    '''

    trimmed_tree = trim_tree(tree)

    '''
    this is what `trimmed_tree` looks like:

    ((('h', 'i'), ('r', ('T', 'b'))), ((('o', 's'), ('t', 'w')), \
        (' ', ('d', 'e'))))
    '''

    return trimmed_tree


def trim_tree(tree):
    '''
     removes frequencies from pseudo min heap
    '''
    leaf = tree[1]

    if type(leaf) == str:
        return leaf
    else:
        return trim_tree(leaf[0]), trim_tree(leaf[1])


def encode(node, branch=''):
    '''
     recursively traverses tree and keeps track of 
     left or right turns (branch) and replaces character in 
     global variable codes (dictionary) for either a 0 or a 1
    '''
    global codes

    if type(node) == str:
        codes[node] = branch
    else:
        encode(node[0], branch + '0')
        encode(node[1], branch + '1')


##############------ DRIVER CODE -----------############
if __name__ == "__main__":
    print()

    codes = {}

    s = "The bird is the word"

    pseudo_heap = generate_pseudo_heap(s)

    tree = build_tree(pseudo_heap)

    encode(tree)

    print()

    print("The size of the data is: {}".format(
        sys.getsizeof(s)))
    print("The content of the data is: {}\n".format(s))

    encoded_data = huffman_encoding(s)

    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(tree, encoded_data)

    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
