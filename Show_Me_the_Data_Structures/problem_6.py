'''
Your task for this problem is to fill out 
the union and intersection functions. 
The union of two sets A and B is the set of elements 
which are in A, in B, or in both A and B. 
The intersection of two sets A and B, denoted by A ∩ B, 
is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list 
that is composed of either the union or intersection, respectively. 
Once you have completed the problem you will 
(i) create your own test cases and 
(ii) perform your own run time analysis on the code.
'''

# inspiration in java: https://www.geeksforgeeks.org/union-and-intersection-of-two-linked-lists/

############------------ IMPORTS ------------############


############------------ FUNCTIONS ------------############
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
        return out_string

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


# def union(llist_1, llist_2):
#     '''
#      creates a variable `n2` to
#      store head and traverse `llist_2`
#      whilst its head isn't `None`, appending
#      each node to `llist_1`
#     '''
#     n2 = llist_2.head

#     while n2 is not None:
#         llist_1.append(n2)
#         n2 = n2.next

#     return llist_1


def intersection(llist_1, llist_2):
    '''
     traverses `llist_1` and searches the value
     of each node in `llist_2`.
     if value in both "llists", appends element 
     to `intersection_llist`
    '''

    intersection_llist = LinkedList()

    head_from_llist_1 = llist_1.head

    while head_from_llist_1 is not None:
        if is_in(llist_2, head_from_llist_1.value):
            intersection_llist.append(head_from_llist_1.value)
        head_from_llist_1 = head_from_llist_1.next

    return intersection_llist


def is_in(llist_2, v):
    head_from_llist_2 = llist_2.head

    while head_from_llist_2 is not None:
        if head_from_llist_2.value == v:
            return True
        head_from_llist_2 = head_from_llist_2.next
    return False

# Test case 1


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

# linked_list_3 = LinkedList()
# linked_list_4 = LinkedList()

# element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
# element_2 = [1, 7, 8, 9, 11, 21, 1]

# for i in element_1:
#     linked_list_3.append(i)

# for i in element_2:
#     linked_list_4.append(i)

# print(union(linked_list_3, linked_list_4))
# print(intersection(linked_list_3, linked_list_4))
