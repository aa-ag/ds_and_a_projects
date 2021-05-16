## TIME COMPLEXITY

`O(n)`

## SPACE COMPLEXITY 

`O(1)`

## Design choices

In this case, the most important choice was to iterate over elements in the array and swap in place to avoid requiring additional space.  In the worst-case scenario, where all items in list are out of order, the algo takes one traversal (all items) to sort the array.