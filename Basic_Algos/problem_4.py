'''
Given an input array consisting on only 0, 1, and 2, 
sort the array in a single traversal. 

You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. 
For e.g. if you traverse the array twice, 
that would still be an O(n) solution but it will not count as single traversal.
'''


############------------ FUNCTIONS ------------############
def sort_012(input_list):
    """
     checks inputs: (i) most be lists, 
     (ii) elements must only be 0, 1 or 2
     places 0's and 2's in correct ends of list, 
     hence leaving 1's in correct place too
    """
    if input_is_valid(input_list) == False:
        raise "Invalid input"


def input_is_valid(input_list):
    """
     checks if input is valid
    """
    if type(input_list) == list and all(i in [0, 1, 2] for i in input_list):
        return True
    return False


############------------ TESTS ------------############
# TEST CASE 1
def test_case_1(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# TEST CASE 2
def test_case_2(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# TEST CASE 3
def test_case_3(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# TEST CASE 4
def test_case_4(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# TEST CASE 5
def test_case_5(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # TEST CASE 1
    test_case_1([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

    # TEST CASE 2
    test_case_2([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
                 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

    # TEST CASE 3
    test_case_3([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    # TEST CASE 4
    test_case_4({0, 0, 0, 0, 0})

    # TEST CASE 5
    test_case_5([0, 1, 2, 0, 1, 2, 5])
