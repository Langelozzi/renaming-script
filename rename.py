# Author: Lucas Angelozzi
# Date: 04/23/22
# Purpose: Script to change file names with spaces to underscores

# Imports
import os
import sys


def replace_spaces(path: str, file: str) -> str:
    f_name, f_ext = os.path.splitext(file)
    old = str(sys.argv[2])
    new = str(sys.argv[3])
    
    if old in str(f_name):
        f_name = f_name.replace(old, new)
        new_name = f"{f_name}{f_ext}"
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
        print(f"{file} --> {new_name}")


def loop_files(start_path):
    path = start_path

    for path, subdirs, files in os.walk(path):
        for dir in subdirs:
            replace_spaces(path, dir)
    for path, subdirs, files in os.walk(path):
        for name in files:
            replace_spaces(path, name)


def main():
    starting_path = sys.argv[1]
    for i in range(0, 100):
        loop_files(starting_path)


if __name__ == "__main__":
    main()