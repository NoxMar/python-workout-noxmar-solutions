#!/usr/bin/env python3
"""
Solution for exercise 32 "flipped_dict" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

from typing import Mapping, Hashable


def flipped_dict(
        dict_: Mapping[Hashable, Hashable]) -> Mapping[Hashable, Hashable]:
    """Returns new dict in which values from original dict are key and vice versa.

    All values in `dict_` need to be hashable. If more than one key has the
    same value the last key encountered during in iteration over `dict_` will
    be the value in the resulting dict.

    Args:
        dict_ (Mapping[Hashable, Hashable): Dict to be flipped. Values must
          be hashable.


    Returns:
        Mapping[Hashable, Hashable]: Mapping in which values from the original
        `dict_` are keys and their corresponding keys their values.
    """
    return {v: k for k, v in dict_.items()}


if __name__ == "__main__":
    print(flipped_dict({"a": 1, "b": 2, "c": 3}))
