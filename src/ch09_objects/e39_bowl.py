#!/usr/bin/env python3
"""
Solution for exercise 39 "bowl" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""
from typing import List
from dataclasses import dataclass, field

from e38_scoop import Scoop  # pylint: disable=import-error


@dataclass(slots=True)
class Bowl:
    """Bowl of ice cream containing scoops.

    Attributes:
        scoops (List[Scoop]): List of scoops contained in this bowl. Should not
          be modified "by hand".
    """
    scoops: List[Scoop] = field(default_factory=list)

    def add_scoops(self, *scoops: tuple[Scoop]):
        """Adds `scoops` to the end of the `scoops` field list of an instance.
        """
        self.scoops.extend(scoops)

    def __repr__(self):
        return f"Bowl() scoops={self.scoops}"

    def __str__(self):
        return "\n".join(scoop.flavor for scoop in self.scoops)


if __name__ == "__main__":
    scoops_ = [
        Scoop(flavor) for flavor in ("chocolate", "vanilla", "persimmon")
    ]

    bowl = Bowl()
    bowl.add_scoops(*scoops_)
    print(bowl)
