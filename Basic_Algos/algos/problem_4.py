############------------ FUNCTIONS ------------############
def sort_012(input_list):
    """
     checks inputs: (i) most be lists,
     (ii) elements must only be 0, 1 or 2
     places 0's and 2's in correct ends of list,
     hence leaving 1's in correct place too
    """

    # if input isn't valid, raise error
    if input_is_valid(input_list) == False:
        raise "Invalid input"

    # set pointers
    # 0 starts at index 0 to move right
    next_position_of_zero = 0
    # 2 starts at second to last index to move left
    next_position_of_2 = len(input_list) - 1
    front_index = 0

    # iterate over and swap elements
    while front_index <= next_position_of_2:
        # if the value in the index is 0
        if input_list[front_index] == 0:
            # swap with next index where value is 0
            input_list[front_index] = input_list[next_position_of_zero]
            # set value in that index to zero
            input_list[next_position_of_zero] = 0
            # and move index the right 1
            next_position_of_zero += 1
            front_index += 1

        # if the value in the index is 2
        elif input_list[front_index] == 2:
            # swap with next index where value is 2
            input_list[front_index] = input_list[next_position_of_2]
            # set value in that index to two
            input_list[next_position_of_2] = 2
            # and move index the left 1
            next_position_of_2 -= 1
        else:
            # otherwise, move one index to the right
            front_index += 1


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
    if input_is_valid(test_case) == False:
        return "invalid input"
    sort_012(test_case)
    if test_case == sorted(test_case):
        return "Pass"
    else:
        return "Fail"


# TEST CASE 2
def test_case_2(test_case):
    if input_is_valid(test_case) == False:
        return "invalid input"
    sort_012(test_case)
    if test_case == sorted(test_case):
        return "Pass"
    else:
        return "Fail"


# TEST CASE 3
def test_case_3(test_case):
    if input_is_valid(test_case) == False:
        return "invalid input"
    sort_012(test_case)
    if test_case == sorted(test_case):
        return "Pass"
    else:
        return "Fail"


# TEST CASE 4
def test_case_4(test_case):
    if input_is_valid(test_case) == False:
        return "invalid input"
    sort_012(test_case)
    if test_case == sorted(test_case):
        return "Pass"
    else:
        return "Fail"


# TEST CASE 5
def test_case_5(test_case):
    if input_is_valid(test_case) == False:
        return "invalid input"
    sort_012(test_case)
    if test_case == sorted(test_case):
        return "Pass"
    else:
        return "Fail"


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # TEST CASE 1
    print(test_case_1([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))

    # TEST CASE 2
    print(test_case_2([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
                       2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))

    # TEST CASE 3
    print(test_case_3([0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))

    # TEST CASE 4
    print(test_case_4({0, 0, 0, 0, 0}))

    # TEST CASE 5
    print(test_case_5([0, 1, 2, 0, 1, 2, 5]))
