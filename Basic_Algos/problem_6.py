'''
In this problem, we will look for smallest
and largest integer from a list of unsorted integers.
The code should run in O(n) time.
Do not use Python's inbuilt functions
to find min and max.

Bonus Challenge: Is it possible
to find the max and min in a single traversal?

Sorting usually requires O(n log n) time
Can you come up with a O(n) algorithm (i.e., linear time)?

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''
############------------ IMPORTS ------------############
import random


############------------ FUNCTIONS ------------############
def get_min_max(integers):
    """
     traverse through the list of intergers once
     and keep track of min and max at each index,
     finally return both
    """
    minimun_integer = 0
    maximun_integer = 0

    for integer in integers:
        if integer > maximun_integer:
            maximun_integer = integer
        if integer < minimun_integer:
            minimun_integer = integer

    return minimun_integer, maximun_integer


############------------ TESTS ------------############
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)


############------------ DRIVER CODE ------------############
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
