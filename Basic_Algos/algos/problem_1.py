############------------ FUNCTIONS ------------############
def sqrt(n):
    """
     perform binary search from 
     1 to a number that is larger than n
     and return value previous to that limit
    """
    # base cases for 0 and 1
    if n in (0, 1):
        return n

    # pointers
    lowerbound = 1
    upperbound = n

    # binary search using while loop
    # from `lowerbound` up to `n`
    while lowerbound <= upperbound:
        middle = (lowerbound + upperbound) // 2

        if middle * middle == n:
            return middle

        if middle * middle < n:
            lowerbound = middle + 1
            answer = middle

        else:
            upperbound = middle - 1

    return answer


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
        return "Pass" if (n == sqrt(1000000)) else "Fail"
    return "Invalid input"


# TEST 6
def test_case_6(n):
    if input_is_valid(n) == True:
        return "N\\A"
    return "Invalid input"


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # TEST 1
    print(test_case_1(3))  # Pass

    # TEST 2
    print(test_case_2(0))  # Pass

    # TEST 3
    print(test_case_3(4))  # Pass

    # TEST 4
    print(test_case_4(1))  # Pass

    # TEST 5
    print(test_case_5(1000))  # Pass

    # TEST 6
    print(test_case_6('this is a string'))
    # Invalid input
