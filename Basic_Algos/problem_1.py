'''
Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27,
the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
'''

'''
# CLUES:
- I think it's possible to get logN with divide and conquer,

simply find the middle number (divide target by 2), and keep dividing it until you find the closest answer.

also the answer is an integer not Float, so it's quite straightforward to find I think.

https://www.ideserve.co.in/learn/time-and-space-complexity-of-recursive-algorithms

https://www.geeksforgeeks.org/binary-search/

https://www.geeksforgeeks.org/square-root-of-an-integer/
'''


############------------ FUNCTIONS ------------############
def sqrt(n):
    """
    creates base case for n = 0/1
    sets a variable i to 1
    to try everything from 1 up to
    i * i >= n
    """

    if n == 0 or n == 1:
        return n

    i = 1
    floored_squared_root = 1

    while floored_squared_root <= n:
        i += 1
        floored_squared_root = i * i

    return i - 1

############------------ TESTS ------------############
# TEST 1


def test_case_1():
    print("Pass" if (3 == sqrt(9)) else "Fail")


# TEST 2
def test_case_2():
    print("Pass" if (0 == sqrt(0)) else "Fail")


# TEST 3
def test_case_3():
    print("Pass" if (4 == sqrt(16)) else "Fail")


# TEST 4
def test_case_4():
    print("Pass" if (1 == sqrt(1)) else "Fail")


# TEST 5
def test_case_5():
    print("Pass" if (5 == sqrt(27)) else "Fail")


# TEST 6
def test_case_6():
    pass


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # TEST 1
    test_case_1()

    # TEST 2
    test_case_2()

    # TEST 3
    test_case_3()

    # TEST 4
    test_case_4()

    # TEST 5
    test_case_5()

    # TEST 6
    test_case_6()
