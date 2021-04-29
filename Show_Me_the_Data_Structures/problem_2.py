############------------ IMPORTS ------------############
import os
from pathlib import Path as p


############------------ FUNCTIONS ------------############
def find_files(suffix, file_path):
    """
     Finds all files beneath path with file name suffix.
    """

    if os.path.exists(file_path):

        answer = list()

        for directory_or_file in p(file_path).rglob(suffix):
            answer.append(directory_or_file.name)

        if not answer:
            return "No files found in the given path"
        return answer

    return "Invalid input path"


############------------ TESTS ------------############
def test_case_1():
    path_to_root_directory = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/testdir'
    suffix = ".test"
    print(find_files(suffix, path_to_root_directory))
    # ['t1.c', 'b.c', 'a.c', 'a.c']


def test_case_2():
    path_to_invalid_input_path = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/thisdirectorydoesnotexists'
    suffix = ".c"
    print(find_files(suffix, path_to_invalid_input_path))
    # Invalid input path


def test_case_3():
    path_to_empty_input_path = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/testdir/subdir2'
    suffix = ".c"
    print(find_files(suffix, path_to_empty_input_path))
    # No files found for the given extension


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    # TEST CASE 1
    test_case_1()

    # TEST CASE 2
    test_case_2()

    # TEST CASE 3
    test_case_3()
