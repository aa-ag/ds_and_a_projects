############------------ IMPORTS ------------############
import heapq


############------------ FUNCTIONS ------------############
def a_star():
    frontier = []
    heapq.heapify(frontier)

    for i in range(20):
        heapq.heappush(frontier, i)

    print(frontier)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    a_star()

'''
f(n) = g(n) + h(n)

g  (n) : The actual cost path from the start node to the current node. 
h (n) : The actual cost path from the current node to goal node.
f  (n) : The actual cost path from the start node to the goal node.
'''
