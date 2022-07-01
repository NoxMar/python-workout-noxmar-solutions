#!/usr/bin/env python3
"""
Solution for exercise 47 "circle" from chapter 9 of "Python Workout" by Reuven M. Lerner
"""

from collections.abc import Iterable, Sized


class Circle(Iterable, Sized):
    """Iterable supplying elements until desired lengths is reached.

    If supplied iterable contains less than desired number of elements, then
    elements would be "looped* desired number of times. For examples iterator
    from `Circle("ab", 5)` would yield `"a", "b", "a", "b", "a"`.
    """

    def __init__(self, iterable: Iterable, length: int):
        """Initializes `Circle` instance supplying `length` items from `iterable`.

        Args:
            iterable (Iterable): Iterable used as a source of the returned items.
            length (int): Number of elements to be returned.
        """
        self._iterable = iterable
        self._length = length

    def __iter__(self):
        n = len(self._iterable)
        return (self._iterable[i % n] for i in range(self._length))

    def __len__(self):
        return self._length


if __name__ == "__main__":
    print(*Circle('abc', 5), sep=", ")
