#!/usr/bin/env python3
"""
Solution for exercise 9 "firstlast" from chapter 3 of "Python Workout" by Reuven M. Lerner
"""

from typing import Sequence


def firstlast(seq: Sequence) -> Sequence:
    """Returns first and last elements from the sequence as sequence.

    If `s` is empty the returned sequence would be as well. For one element
    sequences returned sequence will contain two references to the only element
    in `s`.

    Args:
        s (Sequence): Sequence from which the first and the last elements will
        be returned.

    Returns:
        Sequence: Sequence of the same type as `s` containing first and last
        element of `s`.
    """
    return seq[:1] + seq[-1:]


if __name__ == "__main__":
    str_ = input("Input string:")
    print(f"First and last elements from this string are: `{firstlast(str_)}`")
