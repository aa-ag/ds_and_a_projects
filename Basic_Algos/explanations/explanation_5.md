## TIME COMPLEXITY

`O(W*L)` 

## SPACE COMPLEXITY 

`O(ALPHABET_SIZE * key_length * N)`

## Design choices

After reading a few articles and StackOverflow threads, I learned that Tries have a time complexity of `O(W*L)` "where W is the number of words, and L is an average length of the word: you need to perform L lookups on the average for each of the W words in the set." and a space complexity of `O(ALPHABET_SIZE * key_length * N)` "where N is number of keys in Trie."

Where I tried to gain some speed was in having each `TrieNode` be a `defaultdict`, insert operations are fast -- O(1).

------------

\[1\] https://stackoverflow.com/questions/13032116/trie-complexity-and-searching

\[2\] https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014

\[3\] https://www.cs.cmu.edu/~fp/courses/15122-f10/lectures/18-tries.pdf
