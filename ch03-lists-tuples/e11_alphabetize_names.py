#!/usr/bin/env python3
"""
Solution for exercise 11 "alphabetic_names" from chapter 3 of "Python Workout" by Reuven M. Lerner
"""

import operator
from typing import Iterable, Mapping

_PEOPLE = [{
    'first': 'Reuven',
    'last': 'Lerner',
    'email': 'reuven@lerner.co.il'
}, {
    'first': 'Donald',
    'last': 'Trump',
    'email': 'president@whitehouse.gov'
}, {
    'first': 'Vladimir',
    'last': 'Putin',
    'email': 'president@kremvax.ru'
}]


def alphabetize_names(
        people: Iterable[Mapping[str, str]]) -> Iterable[Mapping]:
    """Returns copy of `people` sorted by last and then first name.

    Sorting is by UTF8 codepoints so it's equivalent of alphabetic sorting for
    Latin alphabet.

    Args:
        people (Iterable[Mapping[str, str]]): Iterable of dicts each of which
        represents a person with the keys meaning:
        - `first` - First name
        - `last` - Last name
        - `email` - Email address

    Returns:
        Iterable[Mapping]: Sorted copy of iterables representing people
        as dictionaries as described in the description of the `people`
        argument.
    """
    return sorted(people, key=operator.itemgetter('last', 'first'))


if __name__ == "__main__":
    print(alphabetize_names(_PEOPLE))
