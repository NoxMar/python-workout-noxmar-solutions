#!/usr/bin/env python3
"""
Solution for exercise 34 "supervocalic" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike
from typing import Set
import sys

_VOWELS_SET = set("aeiou")


def _is_supervocalic(word: str) -> bool:
    letters_in_word = set(word.lower())
    return _VOWELS_SET.issubset(letters_in_word)


def get_sv(path: PathLike) -> Set[str]:
    """Gets all supervocalic words from dict (one word per line) file as a set.

    Word is considered supervocalic if it contains all of the vowels at least
    once. File pointed to by `path` must exist and program has to have
    permissions to read it.

    Args:
        path (PathLike): Path to a dict style (one word per line) file
          containing words to be checked.

    Returns:
        Set[str]: Set of all words from file pointed to by `path` that are
          supervocalic.
    """
    with open(path, encoding='utf-8') as f:
        return {word for line in f if _is_supervocalic(word := line.strip())}


if __name__ == "__main__":
    print(get_sv(sys.argv[1] if len(sys.argv) > 1 else "words.txt"))
