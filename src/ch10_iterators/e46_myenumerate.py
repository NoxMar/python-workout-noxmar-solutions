#!/usr/bin/env python3
"""
Solution for exercise 46 "myenumerate" from chapter 9 of "Python Workout" by Reuven M. Lerner
"""

from collections.abc import Iterable, Iterator


class MyEnumerate(Iterator, Iterable):
    """Instances act similarly to object returned by builtin `enumerate()`.

    Instances can be iterated over **only once**. Following iterations result
    in rising `StopIteration` immediately thus ending iteration yielding 0
    elements.
    """

    def __init__(self, iterable: Iterable):
        """Creates instance that works like return value of `enumerate`.

        Instances can be enumerated over only once.

        Args:
            iterable (Iterable): Iterable to be enumerated.
        """
        self._index = 0
        self._iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        i = self._index
        self._index += 1
        try:
            return i, self._iterable[i]
        except IndexError:
            raise StopIteration()  # pylint: disable=raise-missing-from


def _main():
    e = MyEnumerate('abc')

    print('** A **')
    for index, one_item in e:
        print(f'{index}: {one_item}')

    print('** B **')
    for index, one_item in e:
        print(f'{index}: {one_item}')


if __name__ == "__main__":
    _main()
