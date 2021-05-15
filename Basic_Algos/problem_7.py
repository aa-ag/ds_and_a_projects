'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(ALPHABET_SIZE * key_length * N) where N is number of keys in Trie.
'''

############------------ IMPORTS ------------############
from collections import defaultdict


############------------ CLASSES ------------############
# a Node class for the RouterTrie
class RouterTrieNode:
    def __init__(self, handler=None):
        '''
         Initializes the node with children
         plus a handler
        '''
        self.children = defaultdict(RouterTrieNode)
        self.handler = handler

    def insert(self, node):
        '''
         inserts node to `self.children`
        '''
        self.children[node] = RouterTrieNode()


# A RouteTrie will store our routes
# and their associated handlers
class RouterTrie:
    def __init__(self, handler):
        '''
         Initialize the trie with an root node
         and a handler, this is the root path
         or home page node
        '''
        self.root = RouterTrieNode(handler)

    def insert(self, path, handler):
        '''
         Similar to our previous example
         you will want to recursively add nodes
         Make sure you assign the handler
         to only the leaf (deepest) node of this path
        '''
        node = self.root

        for element in path:
            node.insert(element)
            node = node.children[element]

        node.handler = handler

    def find(self, path):
        '''
         Starting at the root, navigate
         the Trie to find a match for this path
         Find the trie node that represents this path
         Return the handler for a match,
         or None for no match
        '''
        node = self.root

        for i in path:
            if i not in node.children:
                return None
            node = node.children[i]

        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler='404 page not found'):
        '''
         Create a new RouteTrie
         for holding our routes
         You could also add a handler
         for 404 page not found responses as well!
        '''
        self.route_trie = RouterTrie(handler)
        self.not_found_handler = not_found_handler
        self.path_length_in_characters = len(handler)

    def add_handler(self, path, handler):
        '''
         Add a handler for a path
         You will need to split the path
         and pass the pass parts
         as a list to the RouteTrie
         node = self.routeTrie
        '''
        if self.path_length_in_characters + len(path) < 1900:
            elements_in_path = self.split_path(path)
            self.route_trie.insert(elements_in_path, handler)
            self.path_length_in_characters += len(path)
        else:
            raise ValueError("Can't handle that")

    def lookup(self, path):
        '''
         lookup path (by parts) and
         return the associated handler
         you can return None if it's not found or
         return the "not found" handler if you added one
         bonus points if a path works
         with and without a trailing slash
         e.g. /about and /about/ both return the /about handler
        '''
        elements_in_path = self.split_path(path)
        match = self.route_trie.find(elements_in_path)
        if match is None:
            return self.not_found_handler
        return match

    def split_path(self, path):
        '''
         you need to split the path into parts for
         both the add_handler and loopup functions,
         so it should be placed in a function here
        '''
        clean_path = path.replace('/', '')

        if clean_path != '':
            return clean_path.split('/')
        return []


############------------ TESTS ------------############
# TEST CASE 1
def test_case_1():
    r = Router("root handler", "404 page not found")

    r.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(r.lookup("/"))  # should print 'root handler'
    # should print 'not found handler'
    # or None if you did not implement one
    print(r.lookup("/home"))
    print(r.lookup("/home/about"))  # should print 'about handler'
    # should print 'about handler'
    # or None if you did not handle trailing slashes
    print(r.lookup("/home/about/"))
    # should print 'not found handler'
    # or None if you did not implement one
    print(r.lookup("/home/about/me"))


# TEST CASE 2
def test_case_2():
    r = Router("root handler")
    print(r.lookup("/home"))
    # 404 page not found
    print(r.lookup(""))
    # root handler


# TEST CASE 3
def test_case_3():
    r = Router("root handler")
    r.add_handler("/" + ("a" * 1900), "too large")
    # ValueError: Can't handle that
    # https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # TEST CASE 1
    test_case_1()

    # TEST CASE 2
    test_case_2()

    # TEST CASE 3
    test_case_3()
