# Explanations

_What is this_: A paragraph explaining desing choices for each problem solved. 

_instructions_: Your paragraph should not be a detailed walkthrough of the code you provided, but provide your reasoning behind decisions made in the code.  For example, why did you use that data structure? You also need to explain the efficiency (time and space) of your solution.

### problem_1.py

__*Time Complexity*__: O(1)

__*Space Complexity*__: Linear

__Walkthroug__

The most important design choice I made was to use `collections.OrderedDict()` for `cache`.  I did this because all operations involving a dictionary (lookup, insert, etc)
have a worst-case complexity of O(1).  This, would allow `LRU_Cache` to be efficient to insert to and to look up values in and at the same time, it would allow for values to be ordered, and therefore, keep tally of capacity.  

This remains true even while checking for invalid inputs at `if type(capacity) != int or capacity < 0: raise "invalid input"`. 


### problem_2.py

__*Time Complexity*__: O(n)

__*Space Complexity*__: Linear

_Walkthroug_

While using Python's built-in `append()` is amortized O(1),
the algo still loops/globs through the entire path provided as input (where files are stored), including subdirectories and the files saved in them. 

For this excercise, one important design decision was the it would not need 3 test cases, as suffix is provided in excercise.  Another key one was to use Python's pathlib due to the exercise's limitation that ruled out using `os.walk()`.  After this, a for loop that would iterate back and forth recursively between folders and files within provided path seemed like the most efficient way to approach this problem.  A

If any files in the directory or subdirectories exists, they are appended to `answer`, and as a list it requires auxiliary space.  Even so, this was the best alternative to present the result in a readable format as expected in the instructions.

### problem_3.py

__*Time Complexity*__: O(log n)

__*Space Complexity*__: Logarithmic Linear

_Walkthroug_

Each function contains a `docstring` explaning it functionality.  There's a comment after each test-case call in `DRIVER CODE` section, showing the result of the algo too.

In natural language, the logic of the program can be described as: 

(i) first, test cases check if input string is empty, if it is, the whole program stops and lets the user know that there's no data to encode;  if it isn't, 

(ii) the program proceeds to generate a pseudo heap of `tuples` (which are fixed-size) with each character and each character's frequency.  `tuples` 

This is what the pseufo heap looks like:

'''
[(1, 'T'), (1, 'b'), (1, 'o'), (1, 's'), (1, 't'), (1, 'w'), (2, 'd'), (2, 'e'), (2, 'h'), (2, 'i'), (2, 'r'), (4, ' ')]
'''

(iii) After that, a tree is generated, with parent and children nodes to look like this:

'''
(20, ((8, ((4, ((2, 'h'), (2, 'i'))), (4, ((2, 'r'), (2, ((1, 'T'), (1, 'b'))))))), (12, ((4, ((2, ((1, 'o'), (1, 's'))), (2, ((1, 't'), (1, 'w'))))), (8, ((4, ' '), (4, ((2, 'd'), (2, 'e')))))))))
'''

(iv) then that tree is trimmed: 

'''
((('h', 'i'), ('r', ('T', 'b'))), ((('o', 's'), ('t', 'w')), (' ', ('d', 'e'))))
'''

(v) and then, that tree is encoded, creating a new empty string `''` where in each `idex` an econded character from `codes` takes place instead of the original character that was there.

Operations within code (such as `collections.Counter(s)`)
have a run time of O(1), and most have O(n) (for loops, checking conditionals, etc);
however, both Python's `sort()` and `sorted()` have worst-case scenario of O(n log n).  This speef efficiencies make up for an otherwise costly use of space through auxiliary lists, dictionaries and empty strings.


### problem_4.py

__*Time Complexity*__: O(1)

__*Space Complexity*__: Linear

_Walkthroug_

Instructions read "Write a function 
that provides an efficient look up of whether the user is in a group."

To achieve "efficiency", the program sacrifices its ability to look up
elements easily (say by index if `groups` and/or `users` were lists). This also means it neither `groups` nor `users` would allow duplicates, but by using sets, the code 
can and does look up if user in in group very efficently, at a worst-case runtime of O(1).

I also made sure that the function checked for the correct input type.

At the same time, the program generates the need for space of each `groups` and `users` sets and those space needs grow linearly with the amount of elements in each.

### problem_5.py

__*Time Complexity*__: O(1)

__*Space Complexity*__: O(n)

_Walkthroug_

Creating a Block class and a Blockchain, as well as inserting new block into Blockchain
may be pretty efficient but using sha256 to hash a string (even though inputs are small)
is the most expensive part of the code at O(n).

Here, I just implemented a Linked List that would allow for new blocks to be inserted as long as all attributes are provided as per `Block` class.

The `__repr__` method allows to `print`/visualize each block and the entire blockchain. 

Using `hashlib.sha256()` to create each block's hash also requires additional space.  In fact, testing size of `self.data` vs `sha.hexdigest()` using `sys` and `.__sizeof__()` showed that it almost double the size of `self.data`.

Finally, how much memory is needed also a function of the lenth of the blockchain. With each new block, more space is required. 


### problem_6.py

__*Time Complexity*__: O(n)

__*Space Complexity*__: Logarithmic

_Walkthroug_

Since for each (union and intersection), in the worst case scenario all elements of
at least one of the linked lists needs to be checked, runtime is on average O(n)

In this case, surprisingly, adding `__str__` to be able to see/visualize both results was a major facilitator of everything else.  In terms of design, the main decisions were: (i) to use `append` method to append each node from `llist_2` to `llist_1` resulting in everyting in both linked lists, and (ii) using `is_in` to be able to check if a given value is in one of the linked lists, to be able to create their intersection.

For `union()`, first the program checks if both linked lists are empty, and if they are, breaks and returns such info to the user.  If one or the other are empty, the program returns the one that isn't, as that would be their _union_.

Alternatively, it `appends` each element from one list to the other.  This could be made more efficient in future iterations by comparing lists and appending the elements of the shorter list to the longer one.

For `intersection()`, the program perform the same three "empty" checks that `union()` does, and then, creates an empty linked lists to which elements that are in each input-linked-lists are pushed to.


--------------------------------------------------------------------
https://stackoverflow.com/questions/46664007/why-do-tuples-take-less-space-in-memory-than-lists

https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1

https://stackoverflow.com/questions/44598732/how-fast-is-computing-a-hash