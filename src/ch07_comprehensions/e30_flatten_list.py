#!/usr/bin/env python3
"""
Solution for exercise 30 "flatten_list" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable, List


def flatten(iter_of_iters: Iterable[Iterable]) -> List:
    """Returns a list of elements of all iterables from `iter_of_iters`.

    All items in `iter_of_iters` need to be iterable.

    Args:
        iter_of_iters (Iterable[Iterable]): Iterable of iterables to flatten.

    Returns:
        List: List containing elements form iterables contained in
          `iter_of_iters`.
    """
    return [x for iter in iter_of_iters for x in iter]


if __name__ == "__main__":
    print(flatten([(1, 2), (3, 4)]))
