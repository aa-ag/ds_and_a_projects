############------------ IMPORTS ------------############
import collections


############------------ CODE ------------############
class LRU_Cache:

    def __init__(self, capacity):
        '''
         Initialize class variables
        '''
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get_(self, key):
        '''
         Retrieve item from provided key.
         Return -1 if nonexistent.
        '''
        if key in self.cache:
            print(self.cache[key])
        else:
            print(-1)

    def set_(self, key, value):
        '''
         Set the value if the key is not present in the cache.
         If the cache is at capacity remove the oldest item.
        '''

        if len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value
            print(-1)

    def print_cache(self):
        '''
         prints out entire `cache` in terminal
        '''
        print(self.cache)


############------------ DRIVER CODE ------------############
# TEST CASE 1
def test_case_1():
    our_cache = LRU_Cache(5)

    our_cache.set_(1, 1)  # adds 1, 1 to ordered dictionary/cache
    our_cache.set_(2, 2)  # adds 2, 2 to ordered dictionary/cache
    our_cache.set_(3, 3)  # adds 3, 3 to ordered dictionary/cache
    our_cache.set_(4, 4)  # adds 4, 4 to ordered dictionary/cache

    our_cache.get_(1)  # returns 1
    our_cache.get_(2)  # returns 2
    our_cache.get_(9)  # returns -1 because 9 is not present in the cache

    our_cache.set_(5, 5)  # adds 5, 5 to ordered dictionary/cache
    our_cache.print_cache()  # see full object
    our_cache.set_(6, 6)  # returns -1 because the cache reached it's capacity
    # but it also removes oldest item to add 6, 6

    our_cache.print_cache()  # see full object
    our_cache.get_(3)  # returns 3


# TEST CASE 2
def test_case_2():
    our_cache = LRU_Cache([])

    our_cache.set_(1, 1)  # adds 1, 1 to ordered dictionary/cache
    our_cache.set_(2, 2)  # adds 2, 2 to ordered dictionary/cache
    our_cache.set_(3, 3)  # adds 3, 3 to ordered dictionary/cache

    our_cache.print_cache()


# TEST CASE 3
def test_case_3():
    our_cache = LRU_Cache(3)

    our_cache.set_(1, 1)  # adds 1, 1 to ordered dictionary/cache
    our_cache.set_(2, 2)  # adds 2, 2 to ordered dictionary/cache
    our_cache.set_(3, 3)  # adds 3, 3 to ordered dictionary/cache

    our_cache.print_cache


if __name__ == "__main__":
    test_case_1()
    # test_case_2()
    # test_case_3()
