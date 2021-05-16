## TIME COMPLEXITY

`O(n)`

## SPACE COMPLEXITY 

`O(m * n)` where m is the length of the word and n is the number of words

## Design choices

Because `RouterTrieNode` is a `defaultdict`, lookup and insert operations run in `O(1)` time.  However, `RouterTrie` inserts elements in path one by one running in N time. Same with `find()`.