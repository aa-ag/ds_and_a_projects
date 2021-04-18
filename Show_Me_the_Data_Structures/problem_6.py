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


def union(llist_1, llist_2):
    # Your Solution Here
    u = LinkedList()

    n1 = llist_1.head

    while n1 is not None:
        print(n1)
        n1 = n1.next


def intersection(llist_1, llist_2):
    # Your Solution Here
    pass


# Test case 1

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

# Test case 2

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
