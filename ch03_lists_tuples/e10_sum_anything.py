#!/usr/bin/env python3
"""
Solution for exercise 10 "sum_anything" from chapter 3 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable, TypeVar

T = TypeVar("T")


def mysum(*args: Iterable[T]) -> T | tuple:
    """Sums passed arguments. If no arguments are passed, returns empty tuple

    Arguments don't have to be of the same type but **must support
    addition (`+` operator) between one another.**

    Args:
        *args(T): Arguments to be summed. All of them must support addition
        between one another.

    Returns:
        Sum of passed arguments if any were passed. Otherwise returns an
        empty tuple.
    """
    if not args:
        return tuple()

    sum_ = args[0]
    for e in args[1:]:
        sum_ += e
    return sum_


if __name__ == "__main__":
    print(mysum())
    print(mysum(10, 20, 30, 40))
    print(mysum('a', 'b', 'c', 'd'))
    print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))
