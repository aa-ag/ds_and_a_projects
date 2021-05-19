############------------ IMPORTS ------------############
import heapq


############------------ FUNCTIONS ------------############
def a_star():
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, 0)
    print(heap)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    a_star()
