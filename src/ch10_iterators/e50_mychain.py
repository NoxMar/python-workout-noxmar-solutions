#!/usr/bin/env python3
"""
Solution for exercise 50 "my_chain" from chapter 9 of "Python Workout" by Reuven M. Lerner
"""

from typing import Any, Iterable, Tuple, Generator


def my_chain(*iterables: Tuple[Iterable]) -> Generator[Any, None, None]:
    """ Yields all elements form the first `iterables` then the second and so on.

    Works as a simplified version of the `itertools.chain` function.

    Yields:
        Any: Elements from consecutive `iterables` in order.
    """
    for iterable in iterables:
        yield from iterable


if __name__ == "__main__":
    print(*my_chain('abc', [1, 2, 3], {'a': 1, 'b': 2}), sep="\n")
