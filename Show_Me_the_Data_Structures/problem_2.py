############------------ IMPORTS ------------############
import os
from pathlib import Path as p


############------------ GLOBAL VARIABLES ------------############
path_to_root_directory = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/testdir'
suffix = ".c"


path_to_invalid_input_path = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/thisdirectorydoesnotexists'
suffix = ".c"


path_to_empty_input_path = '/Users/aaronaguerrevere/Documents/portfolio/filerecursion/testdir/subdir2'
suffix = ".c"


############------------ FUNCTIONS ------------############
def find_files(suffix, file_path):
    """
     Finds all files beneath path with file name suffix.
    """

    # if len(os.listdir(file_path)) == 0:
    #     return "No files found for the given extension"

    if os.path.exists(file_path):

        answer = list()

        for directory_or_file in p(file_path).rglob('*.c'):
            answer.append(directory_or_file.name)

        if not answer:
            return "No files found for the given extension"
        return answer

    return "Invalid input path"


############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    print(find_files(suffix, path_to_root_directory))
    # ['t1.c', 'b.c', 'a.c', 'a.c']

    print(find_files(suffix, path_to_invalid_input_path))
    # Invalid input path

    print(find_files(suffix, path_to_empty_input_path))
    # No files found for the given extension
