'''
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search.
If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array
and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
'''

"""
Find the index by searching in a rotated sorted array

Args:
    input_list(array), number(int): Input array to search and the target
Returns:
    int: Index or -1
"""


############------------ FUNCTIONS ------------############
#  def rotated_array_search(input_list, number):

def binary_search(input_list, number):
    start_index = 0
    end_index = len(input_list) - 1
    middle_index = 0

    while start_index <= end_index:

        middle_index = (end_index + start_index) // 2

        # If x is greater, ignore left half
        if input_list[middle_index] < number:
            start_index = middle_index + 1

        # If x is smaller, ignore right half
        elif input_list[middle_index] > number:
            end_index = middle_index - 1

        # means x is present at middle_index
        else:
            return middle_index

    # If we reach here, then the element was not present
    return -1


print(binary_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
print(binary_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
print(binary_search([6, 7, 8, 1, 2, 3, 4], 8))
print(binary_search([6, 7, 8, 1, 2, 3, 4], 1))
print(binary_search([6, 7, 8, 1, 2, 3, 4], 10))

# def linear_search(input_list, number):
#     for index, element in enumerate(input_list):
#         if element == number:
#             return index
#     return -1


############------------ TESTS ------------############
# def test_function(test_case):
#     input_list = test_case[0]
#     number = test_case[1]
#     if linear_search(input_list, number) == binary_search(input_list, number):
#         print("Pass")
#     else:
#         print("Fail")


############------------ DRIVER CODE ------------############
# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 10])
