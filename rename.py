# Author: Lucas Angelozzi
# Date: 04/23/22
# Purpose: Script to change keywords/characters in filenames and directory names recursively

# Imports
import os
import sys


def replace_char(path: str, file: str):
    """Replaces the old string with the new string

    Args:
        path (str): the path to the file/dir
        file (str): the name of the file/dir
    """
    
    f_name, f_ext = os.path.splitext(file)
    # The old and new strings passed in as cmd arguments
    old = str(sys.argv[2])
    new = str(sys.argv[3])
    
    if old in str(f_name):
        f_name = f_name.replace(old, new)
        new_name = f"{f_name}{f_ext}"
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
        print(f"{file} --> {new_name}")


def loop_files(start_path: str):
    """Loops through subdirectories and files at a path and calls
    the replace function on each one

    Args:
        start_path (str): the path from which you want to start (root path)
    """

    for path, subdirs, files in os.walk(start_path):
        for dir in subdirs:
            replace_char(path, dir)
    for path, subdirs, files in os.walk(start_path):
        for name in files:
            replace_char(path, name)


def main():
    # The root path passed in as the first cmd argument after the script
    starting_path = str(sys.argv[1])
    for i in range(0, 100):
        loop_files(starting_path)


if __name__ == "__main__":
    main()