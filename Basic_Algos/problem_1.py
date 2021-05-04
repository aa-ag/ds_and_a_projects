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


############------------ IMPORTS ------------############


############------------ FUNCTIONS ------------############
def sqrt(n):
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored squared root
    Returns:
    int: Floored Square Root
    """
    # base case
    if n == 0 or n == 1:
        return n

    # start at 1
    i = 1
    floored_squared_root = 1
    # and try all numbers until
    # i * i >= n

    while floored_squared_root <= n:
        i += 1
        floored_squared_root = i * i

    return i - 1

############------------ TESTS ------------############


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
