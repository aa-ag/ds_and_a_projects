'''
Finding Suffixes¶
Now that we have a functioning Trie, 
we need to add the ability to list suffixes to implement 
our autocomplete feature. To do that, we need to implement 
a new function on the TrieNode object that will return 
all complete word suffixes that exist below it in the trie. 
For example, if our Trie contains the words 
["fun", "function", "factory"] and we ask for suffixes 
from the f node, we would expect to receive 
["un", "unction", "actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, 
try to add the suffixes function below. 
(Hint: recurse down the trie, 
collecting suffixes as you go.)
'''

############------------ IMPORTS ------------############
import collections


############------------ FUNCTIONS ------------############
# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffixes = []
        for char, node in self.children.items():
            if node.isWord:
                suffixes.append(suffix + char)
            if node.children:
                suffixes += node.suffixes(suffix + char)
        return suffixes


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
