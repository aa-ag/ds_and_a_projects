## TIME COMPLEXITY

`O(log(n))`

## SPACE COMPLEXITY 

`O(n)`

## Design choices

There were two key limitations on how I was able to aproach this problem. 

First, using any Python library wasn't allowed. 

Second, the expected time complexity was O(log(n)). 

To meet both criteria, the most time-efficient way to approach the problem was to perform a binary search on an moving "middle" which is set by discarding half of all possible answers.

In its current configuration, the algo only accepts integers as valid inputs.