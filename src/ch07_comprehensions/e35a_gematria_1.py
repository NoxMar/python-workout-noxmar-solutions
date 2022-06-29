#!/usr/bin/env python3
"""
Solution for exercise 35a "gematria_dict" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

import string
from typing import Mapping


def get_letters_positions_dict(
        alphabet: str = string.ascii_lowercase) -> Mapping[str, int]:
    """Returns a dict mapping letters from `alphabet` to their positions (1 based) in it.


    Args:
        alphabet (str, optional): Alphabet from which letters are mapped to
          their positions. Defaults to string.ascii_lowercase.

    Returns:
        Mapping[str, int]: Mapping of letters to their positions in the
          `alphabet`.
    """
    return {letter: i for i, letter in enumerate(alphabet, 1)}


if __name__ == "__main__":
    print(get_letters_positions_dict())
