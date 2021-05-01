# Explanations

_What is this_: A paragraph explaining desing choices for each problem solved. 

_instructions_: Your paragraph should not be a detailed walkthrough of the code you provided, but provide your reasoning behind decisions made in the code.  For example, why did you use that data structure? You also need to explain the efficiency (time and space) of your solution.

### problem_1.py

*Time Complexity*: O(1)

*Space Complexity*: Linear

_Walkthroug_

all operations involving a dictionary (lookup, insert, etc)
have a worst-case complexity of O(1).

The most important design choice I made was to use `collections.OrderedDict()` for `cache`.  This, would allow `LRU_Cache` to be efficient to insert to and to look up values in and at the same time, it would allow for values to be ordered, and therefore, keep tally of capacity. 


### problem_2.py

*Time Complexity*: O(n)

*Space Complexity*: Constant

_Walkthroug_

while using Python's built-in `append()` is amortized O(1)',
the algo still loops/globs through the entire path, including
subdirectories

For this excercise, one important design decision was the it would not need 3 test cases, as suffix is provided in excercise.  Another key one was to use Python's pathlib due to the exercise's limitation that ruled out using `os.walk()`.  After this, a for loop that would iterate back and forth recursively between folders and files within provided path seemed like the most efficient way to approach this problem.  Appending to an `answer` list would be easy and allow for printing (seeing) all matches all at once.


### problem_3.py

*Time Complexity*: O(log n)

*Space Complexity*: Logarithmic Linear

_Walkthroug_

a few operations within code (such as `collections.Counter(s)`)
have a run time of O(1), and most have O(n) (for loops, checking conditionals, etc);
however, both Python's `sort()` and `sorted()` have worst-case scenario of O(n log n)

On this one, I struggled using starting point provided in class so instead I used a collection of tuples to generate the min heap.  That way the data structure would be easier to slice.  Once I made that switch, both encoding and decoding became a matter of iterating over each, the input string and the encoded version to decode. 

###### Also, time complexity should be in order of n.

### problem_4.py

*Time Complexity*: O(1)

*Space Complexity*: Linear

_Walkthroug_

this was an interesting one.  problem instructions read "Write a function 
that provides an efficient look up of whether the user is in a group."
to achieve "efficiency", the code may have to give away the ability to look up
elements easily (say by index if `groups` and/or `users` were lists) and it also meant
neither `groups` nor `users` would allow duplicates, but by using sets, the code 
can and does look up if user in in group very efficently, at a worst-case runtime of O(1)

I also made sure that the function checked for the correct input type.


### problem_5.py

*Time Complexity*: O(1)

*Space Complexity*: O(1)

_Walkthroug_

creating a Block class and a Blockchain, as well as inserting new block into Blockchain
may be pretty efficient but using sha256 to hash a string (even though inputs are small)
is the most expensive part of the code at O(n).''

Here, I just implemented a Linked List that would allow for new blocks to be inserted as long as all attributes are provided as per `Block` class.  Pretty straightfoward.


### problem_6.py

*Time Complexity*: O(n)

*Space Complexity*: Logarithmic

_Walkthroug_

since for each (union and intersection) in the worst case scenario all elements of
at least one of the linked lists needs to be checked, runtime is average O(n)

In this case, surprisingly, adding `__str__` to be able to see/visualize both results was a major facilitator of everything else.  In terms of design, the main decisions were: (i) to use `append` method to append each node from `llist_2` to `llist_1` resulting in everyting in both linked lists, and (ii) using `is_in` to be able to check if a given value is in one of the linked lists, to be able to create their intersection.


--------------------------------------------------------------------

' https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1

'' https://stackoverflow.com/questions/44598732/how-fast-is-computing-a-hash