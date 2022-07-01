#!/usr/bin/env python3
"""
Solution for exercise 48 "all_lines" from chapter 9 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike, listdir, path
import sys
from typing import Generator


def all_lines(directory_path: PathLike) -> Generator[str, None, None]:
    """Returns iterable of all lines in all files in directory.

    Not readable (due to permissions) files are simply skipped. All lines from
    one in the correct order will be returned before the next one, however order
    in which files will be read is not specified.

    Args:
        directory_path (PathLike): Path to the directory from which files are
          to be read from.

    Yields:
        Generator[str, None, None]: Generator of all lines (in order) from all
          files in a given directory.
    """
    for file_name in listdir(directory_path):
        file_path = path.join(directory_path, file_name)
        try:
            with open(file_path, encoding="utf-8") as f:
                yield from f
        except OSError:
            pass


if __name__ == "__main__":
    print(*all_lines(sys.argv[1]), sep="")
