#!/usr/bin/env python3
"""
Solution for exercise 38 "scoop" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Scoop:  # pylint: disable=too-few-public-methods
    """Represents a scoop of ice cream.

    Attributes:
        flavor(str): A string to indicate the flavor of the ice cream scoop.
    """

    flavor: str


def create_scoops() -> None:
    """Creates 3 `Scoop` objects of different valors and displays their flavors.

    Scoops of the following flavors will be created: "chocolate", "vanilla", and
    "persimmon". Flavors will be printed one per line.
    """
    scoops = [
        Scoop(flavor) for flavor in ("chocolate", "vanilla", "persimmon")
    ]
    print(*(scoop.flavor for scoop in scoops), sep="\n")


if __name__ == "__main__":
    create_scoops()
