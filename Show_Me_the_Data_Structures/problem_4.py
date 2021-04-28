############------------ HELPER CODE ------------############
class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


############------------ FUNCTIONS ------------############
def is_user_in_group(user, group):
    """
     Returns True if user is in the group,
     False otherwise.
    """
    try:
        return user in group.get_users()
    except:
        return "Invalid Input"


############------------ TEST CASES ------------############
def test_case_1():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    foo = Group('foo')
    bar = Group('bar')

    sub_child_user = "sub_child_user"
    another_sub_child_user = "another_sub_child_user"

    sub_child.add_user(sub_child_user)
    sub_child.add_user(another_sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    sub_child.add_group(foo)
    sub_child.add_group(bar)

    user_1 = 'sub_child_user'

    print(is_user_in_group(user_1, sub_child))  # True


def test_case_2():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    foo = Group('foo')
    bar = Group('bar')

    sub_child_user = "sub_child_user"
    another_sub_child_user = "another_sub_child_user"

    sub_child.add_user(sub_child_user)
    sub_child.add_user(another_sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    sub_child.add_group(foo)
    sub_child.add_group(bar)

    user_2 = ['sub_child_user_within_list']
    print(is_user_in_group(user_2, sub_child))  # False


def test_case_3():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    foo = Group('foo')
    bar = Group('bar')

    sub_child_user = "sub_child_user"
    another_sub_child_user = "another_sub_child_user"

    sub_child.add_user(sub_child_user)
    sub_child.add_user(another_sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    sub_child.add_group(foo)
    sub_child.add_group(bar)

    user_3 = None

    print(is_user_in_group(user_3, sub_child))  # False


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
