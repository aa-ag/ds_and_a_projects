############------------ HELPER CODE ------------############
class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


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

# Write a function that provides an efficient
# look up of whether the user is in a group.


############------------ FUNCTIONS ------------############
def is_user_in_group(user, group):
    """
    Return True if user is in the group,
    False otherwise.

    Args:
      user(str): user name/id
      group(class:Group):
      group to check user membership against
    """
    print(f"Group name: {group.get_name()}\n")
    print(
        f"Groups within Group: {[i.get_name() for i in group.get_groups()]}\n")
    print(f"Users within group: {group.get_users()}\n")

    print(user in group.get_users())

    '''
    Group name: subchild

    Groups within Group: ['foo', 'bar']

    Users within group: ['sub_child_user', 'another_sub_child_user']

    True
    '''


############------------ DRIVER CODE ------------############
user = 'sub_child_user'

if __name__ == "__main__":
    is_user_in_group(user, sub_child)
