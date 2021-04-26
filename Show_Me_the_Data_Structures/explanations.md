# Explanations

_What is this_: A paragraph explaining desing choices for each problem solved. 

_instructions_: Your paragraph should not be a detailed walkthrough of the code you provided, but provide your reasoning behind decisions made in the code.  For example, why did you use that data structure? You also need to explain the efficiency (time and space) of your solution.

### problem_1.py

The most important design choice I made was to use `collections.OrderedDict()` for `cache`.  This, would allow `LRU_Cache` to be efficient to insert to and to look up values in and at the same time, it would allow for values to be ordered, and therefore, keep tally of capacity. 

### problem_2.py

For this excercise, one important design decision was the it would not need 3 test cases, as suffix is provided in excercise.  Another key one was to use Python's pathlib due to the exercise's limitation that ruled out using `os.walk()`.  After this, a for loop that would iterate back and forth recursively between folders and files within provided path seemed like the most efficient way to approach this problem.  Appending to an `answer` list would be easy and allow for printing (seeing) all matches all at once.

### problem_3.py

On this one, I struggled using starting point provided in class so instead I used a collection of tuples to generate the min heap.  That way the data structure would be easier to slice.  Once I made that switch, both encoding and decoding became a matter of iterating over each, the input string and the encoded version to decode. 

### problem_4.py

this was an interesting one.  problem instructions read "Write a function 
that provides an efficient look up of whether the user is in a group."
to achieve "efficiency", the code may have to give away the ability to look up
elements easily (say by index if `groups` and/or `users` were lists) and it also meant
neither `groups` nor `users` would allow duplicates, but by using sets, the code 
can and does look up if user in in group very efficently. I also made sure that the function checked for the correct input type.

### problem_5.py

Here, I just implemented a Linked List that would allow for new blocks to be inserted as long as all attributes are provided as per `Block` class.  Pretty straightfoward.

### problem_6.py

In this case, surprisingly, adding `__str__` to be able to see/visualize both results was a major facilitator of everything else.  In terms of design, the main decisions were: (i) to use `append` method to append each node from `llist_2` to `llist_1` resulting in everyting in both linked lists, and (ii) using `is_in` to be able to check if a given value is in one of the linked lists, to be able to create their intersection.