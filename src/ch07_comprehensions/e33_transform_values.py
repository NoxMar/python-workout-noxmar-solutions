#!/usr/bin/env python3
"""
Solution for exercise 33 "transform_values" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

from typing import Mapping, Callable, Any


def transform_values(func: Callable[[Any], Any], dict_: Mapping) -> Mapping:
    """Maps all values in the dictionary and returns dict with mapped values.

    Args:
        func (Callable[[Any], Any]): Callable that is applied to each value in
          the dictionary to produce value in the returned dictionary.
        and
        dict_ (Mapping): Mapping from which values are mapped.

    Returns:
        Mapping: Dict with keys from `dict_` and mapped  values.
    """
    return {k: func(v) for k, v in dict_.items()}


if __name__ == "__main__":
    print(transform_values(lambda x: x * x, {"a": 1, "b": 2, "c": 3}))
