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
    l = ''
    r = ''

    s = ''.join(str(i) for i in sorted(input_list, reverse=True))

    return s  # [5, 4, 3, 2, 1]

    # for i in range(len(s)):
    #     if i % 2 == 0:
    #         l += s[i]
    #     else:
    #         r += s[i]

    # return [l, r]


# odd lenght
print(rearrange_digits([1, 2, 3, 4, 5]))
# [542, 31]

# even length
# print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# [964, 852]

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
