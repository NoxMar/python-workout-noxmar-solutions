#!/usr/bin/env python3
"""
Solution for exercise 40 "limited_size_bowl" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

from dataclasses import dataclass
from typing import Iterable, ClassVar

from e38_scoop import Scoop  # disable pylint: disable=import-error
from e39_bowl import Bowl  # disable pylint: disable=import-error


@dataclass(slots=True)
class LimitedBowl(Bowl):
    """Bowl of ice cream containing up to 3 scoops. Adding more has no effect.

    Trying to add more scoops trough `add_scoops` fails silently. Max count of
    scoops is accessible through class field `MAX_SCOOPS`.

    Attributes:
        scoops (List[Scoop]): List of scoops contained in this bowl. Should not
          be modified "by hand".
    """
    MAX_SCOOPS: ClassVar[int] = 3

    def add_scoops(self, *scoops: Iterable[Scoop]):
        """Adds `scoops` to the Bowl respecting the `MAX_SCOOPS` limit.

        Adding more scoops fails silently if adding them would cause bowl to
        hold more than `MAX_SCOOPS` scoops. Call can succeed partially (e.g.
        adding 2 scoops to the bowl holding 2 scoops already adds the first
        scoop and ignores the second).
        """
        max_scoops_to_add = self.MAX_SCOOPS - len(self.scoops)
        self.scoops.extend(scoops[:max_scoops_to_add])


def _main():
    scoop1 = Scoop('chocolate')
    scoop2 = Scoop('vanilla')
    scoop3 = Scoop('persimmon')
    scoop4 = Scoop('flavor 4')
    scoop5 = Scoop('flavor 5')

    bowl = LimitedBowl()
    bowl.add_scoops(scoop1, scoop2)
    bowl.add_scoops(scoop3)
    bowl.add_scoops(scoop4, scoop5)
    print(bowl)


if __name__ == '__main__':
    _main()
