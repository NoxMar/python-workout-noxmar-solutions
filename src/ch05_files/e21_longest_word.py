#!/usr/bin/env python3
"""
Solution for exercise 21 "longest_word" from chapter 5 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike, scandir


def find_longest_word(path: PathLike) -> str:
    """Returns longest word in file pointed by `path`.

    This function treats any string not containing white characters as words.
    File has to exist and program needs permission to read it.

    Args:
        path (PathLike): Path to the file to find the longest word in.

    Returns:
        str: Longest word in file pointed by `path`.

    Raises:
        IOError: File pointed to by the `path` does not exist or is not
        readable (most likely due to permissions).
    """
    longest_word = ""
    with open(path, encoding='utf-8') as f:
        for line in f:
            words = line.split()
            if not words:
                continue

            longest_word_in_line = max(words, key=len)
            if len(longest_word_in_line) > len(longest_word):
                longest_word = longest_word_in_line
    return longest_word


def find_all_longest_words(directory_path: PathLike) -> dict[PathLike, str]:
    """Returns dict mapping file name to longest word in it.

    This function needs permission to read `directory_path` as well as every
    non-directory file in it.

    Args:
        directory_path (PathLike): Path to directory from which all normals
        files will be processed.

    Returns:
        dict[PathLike, str]: Mapping of file names to longest words in
        corresponding files.
    """
    return {
        path.name: find_longest_word(path)
        for path in scandir(directory_path) if path.is_file()
    }


if __name__ == "__main__":
    print(find_all_longest_words("."))
