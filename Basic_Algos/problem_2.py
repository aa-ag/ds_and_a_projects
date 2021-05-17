############------------ FUNCTIONS ------------############
def rotated_array_search(input_list, number):
    # set pointers
    lowerbound = 0
    upperbound = len(input_list)

    # set condition to break out of the loop
    while lowerbound < upperbound:
        # set middle index
        middle = lowerbound + (upperbound - lowerbound)//2
        # base case
        # if the element in the middle index is the number
        # return its index
        if input_list[middle] == number:
            return middle

        if input_list[lowerbound] <= input_list[middle]:
            if number >= input_list[lowerbound] and number < input_list[middle]:
                upperbound = middle
            else:
                lowerbound = middle + 1
        else:
            if number <= input_list[upperbound - 1] and number > input_list[middle]:
                lowerbound = middle + 1
            else:
                upperbound = middle
    # alternatively, the number isn't in the list
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


############------------ TESTS ------------############
def test_function(test_case):

    input_list = test_case[0]
    number = test_case[1]

    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


############------------ DRIVER CODE ------------############
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
