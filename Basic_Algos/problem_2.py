'''
TIME COMPLEXITY: O(log n).
SPACE COMPLEXITY: O(n).
'''


############------------ FUNCTIONS ------------############
def rotated_array_search(input_list, number):
    '''

    '''
    # set pointers
    low = 0
    high = len(input_list)

    # set conditions to break out of the loop
    while low < high:
        # set middle index
        mid = low + (high-low)//2
        # base case
        # if the element in the middle index is the number
        # return its index
        if input_list[mid] == number:
            return mid

        if input_list[low] <= input_list[mid]:
            if number >= input_list[low] and number < input_list[mid]:
                high = mid
            else:
                low = mid+1
        else:
            if number <= input_list[high-1] and number > input_list[mid]:
                low = mid+1
            else:
                high = mid
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
