#!/usr/bin/env python3
"""
Solution for exercise 41 "big_bowl" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

from dataclasses import dataclass
from typing import ClassVar

from e38_scoop import Scoop  # disable pylint: disable=import-error
from e40_limited_size_bowl import LimitedBowl  # disable pylint: disable=import-error


@dataclass(slots=True)
class BigBowl(LimitedBowl):
    """"Bowl of ice cream containing up to 5 scoops.

    Otherwise equivalent to `LimitedBowl`.
    """
    MAX_SCOOPS: ClassVar[int] = 5


def _main():
    scoop1 = Scoop('chocolate')
    scoop2 = Scoop('vanilla')
    scoop3 = Scoop('persimmon')
    scoop4 = Scoop('flavor 4')
    scoop5 = Scoop('flavor 5')
    scoop6 = Scoop('flavor 6')

    bowl = BigBowl()
    bowl.add_scoops(scoop1, scoop2)
    bowl.add_scoops(scoop3)
    bowl.add_scoops(scoop4, scoop5, scoop6)
    print(bowl)


if __name__ == '__main__':
    _main()
