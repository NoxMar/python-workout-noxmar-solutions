#!/usr/bin/env python3
"""
Solution for exercise 29 "sum_numbers" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable


def int_or_none(x: str) -> int | None:
    """Converts x` to int and if the conversion fails returns `None`.

    This function is equivalent to `int(x)` except in case of failure it
    returns `None` instead of raising `ValueError`.
    """
    try:
        return int(x)
    except ValueError:
        return None


def add_numbers(numbers: Iterable[str]) -> int:
    """Sums all strings from `numbers` that are convertible to integer.

    String is considered to be convertible if `int(s)` would return value (and
    not raise exception).

    Args:
        numbers (Iterable[str]): Iterable of strings to be added as ints.

    Returns:
        int: Sum of ints among the `numbers`.
    """
    return sum(num for n_str in numbers
               if (num := int_or_none(n_str)) is not None)


def _main():
    input_strs = input(
        "Input line containing numbers separated by spaces: ").split()
    print(add_numbers(input_strs))


if __name__ == '__main__':
    _main()
