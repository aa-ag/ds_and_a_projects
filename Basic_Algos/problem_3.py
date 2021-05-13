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


############------------ FUNCTIONS ------------############
def mergesort(items):
    # case where input is list of 1
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left = items[:middle_index]
    right = items[middle_index:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered, merged list
    return merged


print(mergesort([4, 6, 2, 5, 9, 8]))
# [2, 4, 5, 6, 8, 9]


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
# test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
