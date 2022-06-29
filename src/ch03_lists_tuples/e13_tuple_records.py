#!/usr/bin/env python3
"""
Solution for exercise 13 "tuple_records" from chapter 3 of "Python Workout" by Reuven M. Lerner
"""

from typing import Tuple, Iterable
import operator

_PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626),
           ('Jinping', 'Xi', 10.603)]


def _format_record(person: Tuple[str, str, float]) -> str:
    return f"{person[1]:10} {person[0]:10} {person[2]:5.2f}"


def format_sort_records(people: Iterable[Tuple[str, str, float]]) -> str:
    """Returns formatted person records one per line, sorted by name.

    Sorting is last then first name by UTF8 codepoints so it's equivalent of
    alphabetic sorting for Latin alphabet. Formatting is done using
    constant width fields with travel time

    Args:
        people (Iterable[Tuple[str, str, float]]): Iterable of tuples, each of
        them represents a person and their travel time in the following format:
        - 0 - First Name as a string
        - 1 - Last Name as a string
        - 2 - Travel time in hours as a float

    Returns:
        str: String comprised of lines representing a person and their travel
        time constant-width fields.
    """
    people_sorted = sorted(people, key=operator.itemgetter(1, 0))
    return "\n".join(_format_record(x) for x in people_sorted)


if __name__ == "__main__":
    print(format_sort_records(_PEOPLE))
