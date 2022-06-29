#!/usr/bin/env python3
"""
Solution for exercise 20 "wc" from chapter 5 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike


# Name was specified in the book, so I decided to not change it.
def wc(path: PathLike) -> None:  # pylint: disable=invalid-name
    """Prints number of lines, words and unique words in file pointed by `path`.

    File has to exist and program needs permission to read it.

    Args:
        path (PathLike): Path to the file for which those characteristics are
        to be determined.

    Raises:
        IOError: File pointed to by the `path` does not exist or is not
        readable (most likely due to permissions).
    """
    line_count = 0
    word_count = 0
    unique_words = set()

    with open(path, encoding='utf-8') as f:
        for line in f:
            line_count += 1
            line_words = line.strip().split()
            word_count += len(line_words)
            unique_words.update(line_words)

    print("Number of:",
          f"\tlines={line_count}",
          f"\twords={word_count}",
          f"\tunique words={len(unique_words)}",
          sep="\n")


if __name__ == "__main__":
    wc("wcfile.txt")
