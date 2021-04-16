############------------ INSTRUCTIONS ------------############
'''
For this problem, the goal is to write code for finding 
all files under a directory (and all directories beneath it)
 that end with ".c"
'''

############------------ IMPORTS ------------############
import os


############------------ GLOBAL VARIABLES ------------############
path_to_root_directory = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/testdir'
suffix = ".c"


############------------ FUNCTIONS ------------############
def find_files(s, p):
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

    all_files = list()

    for (root, directories, files) in os.walk(p, topdown=True):
        for each_file in files:
            if each_file.endswith(s):
                all_files.append(each_file)

    print(all_files)
    # ['t1.c', 'b.c', 'a.c', 'a.c']


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    find_files(suffix, path_to_root_directory)


## Locally save and call this file ex.py ##
# Code to demonstrate the use of some of the OS modules in python
# Let us print the files in the directory in which you are running this script
# print(os.listdir("."))

# Let us check if this file is indeed a file!
# print(os.path.isfile("./ex.py"))

# Does the file end with .py?
# print("./ex.py".endswith(".py"))

'''
['testdir', 'ex.py']
True
True
'''
