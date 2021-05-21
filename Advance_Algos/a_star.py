############------------ IMPORTS ------------############
import heapq


############------------ HELPER CODE ------------############
class PriorityQueue:

    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heapq.heappush(self.heap, (0, value))


############------------ FUNCTIONS ------------############


def a_star():
    pass


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    a_star()

'''
f(n) = g(n) + h(n)

g  (n) : The actual cost path from the start node to the current node. 
h (itn) : The actual cost path from the current node to goal node.
f  (n) : The actual cost path from the start node to the goal node.
'''
