############------------ IMPORTS ------------############
import heapq


############------------ HELPER CODE ------------############
class PriorityQueue:

    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heapq.heappush(self.heap, (0, value))

    def enqueue(self, value, priority=0):
        heapq.heappush(self.heap, (priority, value))

    def dequeque(self):
        priority, value = heapq.heappop(self.heap)
        return value

    def __str__(self):
        return self.heap.__str__()

    def size(self):
        return len(self.heap)


############------------ FUNCTIONS ------------############
def test_priority_queue():

    priority_queue = PriorityQueue()

    priority_queue.enqueue(0, 1)
    priority_queue.enqueue(0, 2)
    priority_queue.enqueue(0, 2)

    print(priority_queue)
    # [(1, 0), (2, 0), (2, 0)]

    print(priority_queue.size())
    # 3


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    test_priority_queue()
