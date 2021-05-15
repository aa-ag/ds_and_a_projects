'''
TIME COMPLEXITY: O(W*L), 
                    where W is the number of words, 
                    and L is an average length of the word: 
                    you need to perform L lookups on the average 
                    for each of the W words in the set
SPACE COMPLEXITY: O(ALPHABET_SIZE * key_length * N) where N is number of keys in Trie.
https://stackoverflow.com/questions/13032116/trie-complexity-and-searching
https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
https://www.cs.cmu.edu/~fp/courses/15122-f10/lectures/18-tries.pdf
'''

############------------ IMPORTS ------------############
from collections import defaultdict


############------------ FUNCTIONS ------------############
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def suffixes(self, suffix=''):
        suffixes = []
        for character, node in self.children.items():
            if node.is_word:
                suffixes.append(suffix + character)
            if node.children:
                suffixes += node.suffixes(suffix + char)

        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for character in word:
            node = node.children[character]
        node.is_word = True

    def exists(self, word):
        node = self.find(word)
        return node.is_word if node else False

    def find(self, prefix):
        node = self.root
        for character in prefix:
            if character in node.children:
                node = node.children[character]
            else:
                return None
        return node


############------------ TESTS ------------############
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')
