#!/usr/bin/env python3
"""
Solution for exercise 28 "join_numbers" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable


def join_numbers(numbers: Iterable[int | float]) -> str:
    """Returns string containing `numbers` separated by `,`. Order is preserved.

    Args:
        numbers (Iterable[int  |  float]): Numbers to be joined.

    Returns:
        str: String contacting `numbers` separated by `,`.
    """
    return ",".join(str(n) for n in numbers)


if __name__ == "__main__":
    print("Joined int from 1 to 100 (both inclusive):")
    print(join_numbers(range(1, 101)))
