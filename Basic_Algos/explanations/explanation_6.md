## TIME COMPLEXITY

`O(n)`

## SPACE COMPLEXITY 

`O(1)`

## Design choices

With exercise limitations being:

(i) The code should run in O(n) time. 
(ii) Do not use Python's inbuilt functions to find min and max.

What seemed like a sensible approach was to set some "trackers" using the absolute first element in any given input list/array, as long as they are indeed valid inputs (non-empty, list of integers) and iterate over each element in the list keeping track of whether the next element is heigher or lower than that first value-tracker.

This way, using very little additional space, in one traversal we can were able to find all tests without worrying about if the list was sorted.