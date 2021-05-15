############------------ FUNCTIONS ------------############
def merge(left, right):
    '''
     this helper function merges two sorted halfs
     resulting from `mergesort()` function
    '''
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


def mergesort(list):
    '''
     divides list into 2, 
     calls itself to sort each half, 
     and then merges the two sorted halves
    '''
    # case where input is list of 1
    if len(list) <= 1:
        return list

    middle_index = len(list) // 2
    left = list[:middle_index]
    right = list[middle_index:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def rearrange_digits(input_list):
    '''
     sorts input list using mergesort
     then uses divide and conquer to 
     generate two largest sums 
    '''

    sorted_list = mergesort(input_list)

    input_length = len(input_list)

    if input_length % 2 == 0:
        first_integer = 0
        second_integer = 0

        number_of_digits = input_length // 2

        for i in range(number_of_digits):
            first_integer += (10 ** i) * sorted_list.pop(0)
            second_integer += (10 ** i) * sorted_list.pop(0)

    else:
        first_integer = 0
        second_integer = 0

        number_of_digits = input_length // 2

        for i in range(number_of_digits):
            first_integer += (10 ** i) * sorted_list.pop(0)
            second_integer += (10 ** i) * sorted_list.pop(0)

        first_integer += (10 ** (i + 1)) * sorted_list.pop(0)

    return [first_integer, second_integer]


def is_input_valid(input):
    '''
     checks if input is type list,
     not empty and has less than 10 elements
    '''
    if type(input) == list \
        and len(input) >= 1 \
            and len(input) < 10:
        return True
    return False


############------------ TESTS ------------############
# TEST CASE 1
def test_case_1(test_case):
    if is_input_valid(test_case) == False:
        print("Invalid input")
        return

    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# TEST CASE 2
def test_case_2(test_case):
    if is_input_valid(test_case) == False:
        print("Invalid input")
        return

    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# TEST CASE 3
def test_case_3(test_case):
    if is_input_valid(test_case) == False:
        print("Invalid input")
        return

    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# TEST CASE 4
def test_case_4(test_case):
    if is_input_valid(test_case) == False:
        print("Invalid input")
        return

    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # TEST CASE 1
    test_case_1([[1, 2, 3, 4, 5], [542, 31]])
    # Pass

    # TEST CASE 2
    test_case_2([[4, 6, 2, 5, 9, 8], [964, 852]])
    # Pass

    # TEST CASE 3
    test_case_3([])
    # Invalid input

    # TEST CASE 4
    test_case_4([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    # Invalid input
