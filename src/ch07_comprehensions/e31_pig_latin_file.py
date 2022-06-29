#!/usr/bin/env python3
"""
Solution for exercise 30 "pig_latin_file" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

import sys
from os import PathLike

from ..ch02_strings.e06_pig_latin_sentence import pl_sentence


def translate_file_to_pig_latin(path: PathLike) -> str:
    """Returns `path` contents(lowercase ascii supported) translated to pig latin.

    File pointed to by `path` must exist and be readable. Lines in the resulting
    string will have `\\n` line ending. Multiple white characters between words
    will be replaced with a single space.

    Args:
        path (PathLike): Path to the file to be translated. File must exist and
          be readable.

    Returns:
        str: Contents of the file translated to pig latin (note limitations
          mentioned above).
    """
    with open(path, encoding='utf-8') as f:
        return "\n".join(pl_sentence(line.rstrip("\r\n")) for line in f)


if __name__ == "__main__":
    print(translate_file_to_pig_latin(sys.argv[1]))
