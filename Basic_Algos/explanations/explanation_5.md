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