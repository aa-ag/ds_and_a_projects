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


def input_is_valid(n):
    '''
     checks if input `n` is valid (int)
    '''
    if type(n) == int:
        return True
    return False


############------------ TESTS ------------############
# TEST 1
def test_case_1(n):
    if input_is_valid(n) == True:
        return "Pass" if (n == sqrt(9)) else "Fail"
    return "Invalid input"


# TEST 2
def test_case_2(n):
    if input_is_valid(n) == True:
        return "Pass" if (n == sqrt(0)) else "Fail"
    return "Invalid input"


# TEST 3
def test_case_3(n):
    if input_is_valid(n) == True:
        return "Pass" if (n == sqrt(16)) else "Fail"
    return "Invalid input"


# TEST 4
def test_case_4(n):
    if input_is_valid(n) == True:
        return "Pass" if (n == sqrt(1)) else "Fail"
    return "Invalid input"


# TEST 5
def test_case_5(n):
    if input_is_valid(n) == True:
        return "Pass" if (n == sqrt(27)) else "Fail"
    return "Invalid input"


# TEST 6
def test_case_6(n):
    if input_is_valid(n) == True:
        return "N\\A"
    return "Invalid input"


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # TEST 1
    print(test_case_1(3))

    # TEST 2
    print(test_case_2(0))

    # TEST 3
    print(test_case_3(4))

    # TEST 4
    print(test_case_4(1))

    # TEST 5
    print(test_case_5(5))

    # TEST 6
    print(test_case_6('this is a string'))
