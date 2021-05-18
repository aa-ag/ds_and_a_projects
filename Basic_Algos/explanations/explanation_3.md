## TIME COMPLEXITY

`O(n log n)`

## SPACE COMPLEXITY 

`O(n)`

## Design choices

Implementing merge sort with arrays (lists) passed all tests, in `O(n log n)`.

MergeSort takes `O(n)` space because it basically combines "O(n)" items.  Even though recursion is used, the call stack is called for list halves, and merged into temporary lists, keeping space at `O(n)`.

In future iterations, I read a StackOverflow thread where comments suggest a linked list implementation may improve the algo's space complexity: https://stackoverflow.com/questions/10342890/merge-sort-time-and-space-complexity

---------
\[1\] https://webdocs.cs.ualberta.ca/~holte/mergesort.pdf

\[2\] https://www.interviewcake.com/concept/java/merge-sort