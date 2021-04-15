############------------ INSTRUCTIONS ------------############
'''
For this problem, the goal is to write code for finding 
all files under a directory (and all directories beneath it)
 that end with ".c"
'''

############------------ IMPORTS ------------############
import os


############------------ GLOBAL VARIABLES ------------############
path_to_root_directory = '/Users/aaronaguerrevere/Documents/portfolio/ds_and_a_projects/testdir'


############------------ FUNCTIONS ------------############
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    global


############------------ DRIVER CODE ------------############
## Locally save and call this file ex.py ##
# Code to demonstrate the use of some of the OS modules in python
# Let us print the files in the directory in which you are running this script
print(os.listdir("."))

# Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

# Does the file end with .py?
print("./ex.py".endswith(".py"))

'''
['testdir', 'ex.py']
True
True
'''
