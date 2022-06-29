#!/usr/bin/env python3
"""
Solutions for exercise 2 "mysum" from chapter 1 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable
from numbers import Number


def mysum(*numbers: Iterable[Number]) -> Number:
    """Returns the sum of all numbers passed as arguments.

    Args:
        *numbers: Numbers (as in numbers.Number) to be summed.

    Returns:
        Sum of this function's arguments.

    """

    sum_ = 0
    for number in numbers:
        sum_ += number
    return sum_
