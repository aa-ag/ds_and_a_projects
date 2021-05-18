## TIME COMPLEXITY

`O(log(n))`

## SPACE COMPLEXITY 

`O(1)`

## Design choices

There were two key limitations on how I was able to aproach this problem. 

First, using any Python library wasn't allowed. 

Second, the expected time complexity was `O(log(n))`. 

To meet both criteria, the most time-efficient way to approach the problem was to perform a binary search on an moving "middle" which is set by discarding half of all possible answers.

In its current configuration, the algo only accepts integers as valid inputs.

Finally, because I decided to write an iterative implementation which doesn't require any auxiliary space, the algorithm requires a space complexity of `O(1)`.  This was on purpose, as the recursive solution to this problem would require `O(log N)` space.

---------

\[1\] https://iq.opengenus.org/binary-search-iterative-recursive/

