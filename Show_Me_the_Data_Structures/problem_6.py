############------------ HELPER CODE ------------############
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_head = self.head
        out_string = ""
        while current_head:
            out_string += str(current_head.value) + " -> "
            current_head = current_head.next
        return out_string.rstrip(' -> ')

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def is_in(llist, v):
    '''
     accepts linked list `llist` and value `v`
     traverses the linked lists and if the value
     of one of the nodes equals `v` returns boolean True
     else, returns False after there are no more nodes
    '''
    head_from_llist = llist.head

    while head_from_llist is not None:
        if head_from_llist.value == v:
            return True
        head_from_llist = head_from_llist.next
    return False


############------------ FUNCTIONS ------------############
def union(llist_1, llist_2):
    '''
     creates a variable `h2` to
     store head and traverse `llist_2`
     whilst its head isn't `None`, appending
     each node to `llist_1`
    '''
    if llist_1.size() == 0 and llist_2.size() == 0:
        return "Both lists are empty"

    if llist_1.size() == 0 and llist_2.size() > 0:
        return llist_2

    if llist_1.size() > 0 and llist_2.size() == 0:
        return llist_1

    h2 = llist_2.head

    while h2 is not None:
        llist_1.append(h2)
        h2 = h2.next

    return llist_1


def intersection(llist_1, llist_2):
    '''
     traverses `llist_1` and searches the value
     of each node in `llist_2`.
     if value in both "llists", appends element 
     to `intersection_llist`
    '''
    if llist_1.size() == 0 and llist_2.size() == 0:
        return "Both lists are empty"

    if llist_1.size() == 0 and llist_2.size() > 0:
        return llist_2

    if llist_1.size() > 0 and llist_2.size() == 0:
        return llist_1

    intersection_llist = LinkedList()

    head_from_llist_1 = llist_1.head

    while head_from_llist_1 is not None:
        if is_in(llist_2, head_from_llist_1.value) \
                and not is_in(intersection_llist, head_from_llist_1.value):
            intersection_llist.append(head_from_llist_1.value)
        head_from_llist_1 = head_from_llist_1.next

    if intersection_llist.size() == 0:
        print("N\A")

    return intersection_llist


############------------ TESTS ------------############
# Test case 1
def test_case_1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))
    print()

    '''
     3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1
     4 -> 6 -> 21
    '''


# Test case 2
def test_case_2():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
    print()

    '''
     3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1
     N\A
    '''


# Test case 3
def test_case_3():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
    '''
     Both lists are empty
     Both lists are empty
    '''


# Test case 4
def test_case_4():
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [1, 2, 3, 4, 5, 6]
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_5.append(i)

    print(union(linked_list_5, linked_list_6))
    print(intersection(linked_list_5, linked_list_6))
    '''
     1 -> 2 -> 3 -> 4 -> 5 -> 6
     1 -> 2 -> 3 -> 4 -> 5 -> 6
    '''


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # TEST CASE 1
    test_case_1()

    # TEST CASE 2
    test_case_2()

    # TEST CASE 3
    test_case_3()

    # TEST CASE 4
    test_case_4()
