#!/usr/bin/env python3
"""
Solution for exercise 49 "elapsed_since" from chapter 9 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable, Generator, Tuple
import time


def elapsed_since(
        iterable: Iterable) -> Generator[Tuple[float, any], None, None]:
    """Returns generator of delta from last access and next element from `iterable`.

    Work similarly to `enumerate` but the first value in yielded tuple is time
    in seconds since the previous element was yielded. This value is always of
    o float type ond for the first tuple it is always `0.0`. Second values in
    those tuples will be the consecutive elements from the `iterable`.

    Args:
        iterable (Iterable): Iterable source for second elements of yielded
          tuples.

    Yields:
        Tuple[float, any]: Tuples consisting of a delta in seconds (as a float)
          since the previous element was yielded and the next element from the
          `iterable`.
    """
    previous_time = current_time = time.perf_counter()
    for e in iterable:
        delta = current_time - previous_time
        previous_time = time.perf_counter()
        yield delta, e
        current_time = time.perf_counter()


if __name__ == '__main__':
    for t, e_ in elapsed_since("abcd"):
        print(f"{t}:{e_}")
