############------------ IMPORTS ------------############
import sys
import heapq as hq

############------------ FUNCTIONS ------------############

# PHASE I - Build the Huffman Tree
# I.a: determine frequency of each character in string
s = "AAAAAAABBBCCCCCCCDDEEEEEE"

count = {}

for i in s:
    count[i] = s.count(i)

heap = [j[0] for j in sorted(count.items(), key=lambda i: i[1])]

# create empty heap
hq.heapify(heap)

print(heap)

element = hq.heappop(heap)
print(element)

# def huffman_encoding(data):
#     pass


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
