'''
Rearrange Array Elements so as to form two number 
such that their sum is maximum. Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. 

You're not allowed to use any sorting function that Python provides 
and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. 
Another expected answer can be [542, 31]. 
In scenarios such as these when there are more 
than one possible answers, return any one.
'''
############------------ IMPORTS ------------############


############------------ FUNCTIONS ------------############
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    middle = len(input_list) // 2

    left = input_list[middle:]
    right = input_list[:middle]

    return left, right


# odd lenght
print(rearrange_digits([1, 2, 3, 4, 5]))
# even length
print(rearrange_digits([4, 6, 2, 5, 9, 8]))

############------------ TESTS ------------############
# def test_function(test_case):
#     output = rearrange_digits(test_case[0])
#     solution = test_case[1]
#     if sum(output) == sum(solution):
#         print("Pass")
#     else:
#         print("Fail")


############------------ DRIVER CODE ------------############
# test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
