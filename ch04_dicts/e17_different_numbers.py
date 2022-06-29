#!/usr/bin/env python3
"""
Solution for exercise 17 "different_numbers" from chapter 4 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable, Hashable


def how_many_different_numbers(iterable: Iterable[Hashable]) -> int:
    """Returns the count of unique (**hashable**)elements from the `iterable`.

    Args:
        iterable (Iterable[Hashable]): Iterable of hashable elements from which
        unique elements are counted.

    Returns:
        int: Count of unique elements in `iterable`.
    """
    return len(set(iterable))


if __name__ == "__main__":
    str_ = input("String im which unique elements are to be counted in:")
    unique_count = how_many_different_numbers(str_)
    print(f"This string contains {unique_count} unique elements.")
