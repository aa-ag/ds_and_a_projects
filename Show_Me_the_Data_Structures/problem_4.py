'''
 In Windows Active Directory,
 a group can consist of user(s) and group(s) themselves.
 We can construct this hierarchy as such.
 Where User is represented by str representing their ids.
'''

# removed () & "object" per
# https://docs.python.org/3/tutorial/classes.html


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
snacks = Group('snacks')

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
sub_child.add_group(snacks)

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
    print(group.get_name())
    print([i.get_name() for i in group.get_groups()])
    print(group.get_users())

    '''
    subchild
    []
    ['sub_child_user']
    '''


############------------ DRIVER CODE/TESTS ------------############
user = 'foobar'

if __name__ == "__main__":
    is_user_in_group(user, sub_child)
