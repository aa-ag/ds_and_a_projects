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


############------------ HELPER CODE ------------############
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
user_1 = 'sub_child_user'
user_2 = ['sub_child_user_within_list']
user_3 = None


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print(is_user_in_group(user_1, sub_child))  # True
    print(is_user_in_group(user_2, sub_child))  # False
    print(is_user_in_group(user_3, sub_child))  # False
