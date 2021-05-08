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

    minimun_integer = integers[0]
    maximun_integer = integers[0]

    for integer in integers:
        if integer > maximun_integer:
            maximun_integer = integer
        if integer < minimun_integer:
            minimun_integer = integer

    return minimun_integer, maximun_integer


def input_is_valid(integers):
    """
     checks if input `integers` is valid (list)
    """
    if integers and type(integers) == list:
        return True
    return False


############------------ TESTS ------------############
# TEST CASE 1
def test_case_1():
    # a list containing 0 - 1001
    integers = [i for i in range(0, 1001)]
    # checks if input is valid type
    if input_is_valid(integers) == False:
        return "Invalid input type"
    # shuffintegerse them randomly
    random.shuffle(integers)
    # pass if min is 0 and max is 9
    return "Pass" if ((0, 1000) == get_min_max(integers)) else "Fail"


# TEST CASE 2
def test_case_2():
    integers = [0]
    if input_is_valid(integers) == False:
        return "Invalid input type"
    random.shuffle(integers)
    return "Pass" if ((0, 0) == get_min_max(integers)) else "Fail"


# TEST CASE 3
def test_case_3():
    integers = [i for i in range(-10, 0)]
    if input_is_valid(integers) == False:
        return "Invalid input type"
    random.shuffle(integers)
    return "Pass" if ((-10, -1) == get_min_max(integers)) else "Fail"


# TEST CASE 4
def test_case_4():
    integers = 'this is a string'
    if input_is_valid(integers) == False:
        return "Invalid input type"
    random.shuffle(integers)
    return "Pass" if ((0, 0) == get_min_max(integers)) else "Fail"


# TEST CASE 5
def test_case_5():
    integers = 'this is a string'
    if input_is_valid(integers) == False:
        return "Invalid input type"
    random.shuffle(integers)
    return "Pass" if ((0, 0) == get_min_max(integers)) else "Fail"


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # TEST CASE 1
    print(test_case_1())  # Pass

    # TEST CASE 2
    print(test_case_2())  # Pass

    # TEST CASE 3
    print(test_case_3())  # Pass

    # TEST CASE 4
    print(test_case_4())  # Invalid input type

    # TEST CASE 5
    print(test_case_5())  # Invalid input type
