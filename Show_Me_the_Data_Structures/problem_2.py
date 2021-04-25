############------------ IMPORTS ------------############
import os
from pathlib import Path as p


############------------ GLOBAL VARIABLES ------------############
path_to_root_directory = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/testdir'
suffix = ".c"


############------------ FUNCTIONS ------------############
def find_files(s, path_to_root_directory):
    """
     Finds all files beneath path with file name suffix.
    """

    answer = list()

    for directory_or_file in p(path_to_root_directory).rglob('*.c'):
        answer.append(directory_or_file.name)

    print(answer)
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
