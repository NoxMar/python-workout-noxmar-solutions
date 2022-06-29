#!/usr/bin/env python3
"""
Solution for exercise 16 "dictdiff" from chapter 4 of "Python Workout" by Reuven M. Lerner
"""

from typing import List


def dictdiff(first: dict, second: dict) -> dict[List]:
    """Returns dict of lists k:[first[k], second[k]] if values for k differ.

    The lists include value from `first` as the first element and from second
    as the `second` one. If one of the dicts contains value but the other does
    not place for value from this dict will be filled with `None`.

    Args:
        first (dict): Source for values for the first items in the resulting
        dict.
        second (dict): Source for values for the second items in the resulting
        dict.

    Returns:
        dict[List]: Dictionary of lists representing differences between first
        and second dict.
    """
    keys = first.keys() | second.keys()
    return {
        k: [first.get(k), second.get(k)]
        for k in keys if first.get(k) != second.get(k)
    }


if __name__ == "__main__":
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    print(dictdiff(d1, d1))
    print(dictdiff(d1, d2))

    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}
    print(dictdiff(d3, d4))

    d5 = {'a': 1, 'b': 2, 'd': 4}
    print(dictdiff(d1, d5))
