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
