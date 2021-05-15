# A RouteTrie will store our routes and
# their associated handlers
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children
        # as before, plus a handler
        self.children = dict()
        self.handler = handler

    def insert(self, path, handler):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)
        # The Router class will wrap the Trie
        # and handle


class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node
        # and a handler, this is the root path
        # or home page node
        self.root = RouteTrieNode()
        self.root.children['/'] = RouteTrieNode(handler)

    def insert(self, path, handler):
        # Similar to our previous example you will
        # want to recursively add nodes
        # Make sure you assign the handler
        # to only the leaf (deepest) node of this path
        node = self.root

        for i in path:
            if i == '':
                continue
            if i not in node.children:
                node.children[i] = RouteTrieNode()
            node = node.children[i]
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie
        # to find a match for this path
        # Return the handler for a match,
        # or None for no match

        # A RouteTrieNode will be similar to our
        # autocomplete TrieNode...
        # with one additional element, a handler.
        if len(path) == 0:
            return None

        node = self.root

        for i in path:
            if i not in node.children:
                return None
            node = node.children[i]

        return node.handler


class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding
        # our routes
        # You could also add a handler for 404
        # page not found responses as well!
        RouteTrie.__init__(self, root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and
        # pass the pass parts
        # as a list to the RouteTrie
        elements_in_path = self.split_path(path)
        self.insert(elements_in_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return
        # the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and
        # without a trailing slash
        # e.g. /about and /about/ both return
        # the /about handler
        elements_in_path = self.split_path(path)
        return self.find(elements_in_path)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == '/':
            return [path]

        return path.split('/')


# Here are some test cases and expected outputs
# you can use to test your implementation
# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler'
# or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler'
# or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler'
# or None if you did not implement one
print(router.lookup("/home/about/me"))
