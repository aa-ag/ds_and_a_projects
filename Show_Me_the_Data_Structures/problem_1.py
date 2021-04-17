############------------ IMPORTS ------------############
import collections


############------------ CODE ------------############
class LRU_Cache():

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        # Retrieve item from provided key.
        # Return -1 if nonexistent.
        if key in self.cache:
            print(self.cache[key])
        else:
            print(-1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value
            print(-1)

    def print_cache(self):
        print(self.cache)


############------------ DRIVER CODE ------------############
our_cache = LRU_Cache(5)

our_cache.set(1, 1)  # adds 1, 1 to ordered dictionary/cache
our_cache.set(2, 2)  # adds 2, 2 to ordered dictionary/cache
our_cache.set(3, 3)  # adds 3, 3 to ordered dictionary/cache
our_cache.set(4, 4)  # adds 4, 4 to ordered dictionary/cache

our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)  # adds 5, 5 to ordered dictionary/cache
our_cache.print_cache()  # see full object
our_cache.set(6, 6)  # returns -1 because the cache reached it's capacity

our_cache.print_cache()  # see full object
our_cache.get(3)  # returns 3 was the least recently used entry
