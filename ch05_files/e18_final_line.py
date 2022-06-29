#!/usr/bin/env python3
"""
Solution for exercise 18 "final_line" from chapter 5 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike


def final_line(file_path: PathLike) -> str:
    """Returns final line of the text file passed by `file_path`.

    This line is not modified in any way so keep in mind it might contain
    a new line character at the end. To do this file must exists and the
    program needs to have permission to at least read from it. UTF-8 encoding
    is assumed.

    Args:
        file_path (PathLike): Path of the file to be read to get last line of.

    Returns:
        str: Last line of the file specified to by `file_path`.

    Raises:
        IOError: File pointed to by the `file_path` does not exist or is not
        readable (most likely due to permissions).
    """
    last_line = ""
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            last_line = line
    return last_line


if __name__ == "__main__":
    print(final_line("/etc/passwd"), end="")
