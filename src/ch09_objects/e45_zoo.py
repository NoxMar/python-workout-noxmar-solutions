#!/usr/bin/env python3
"""
Solution for exercise 45 "zoo" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

from dataclasses import dataclass, field
from typing import List, Generator

from e43_animals import Animal, Wolf, Sheep, Parrot, Snake  # pylint: disable=import-error
from e44_cages import Cage  # pylint: disable=import-error


@dataclass
class Zoo:
    """Zoo containing list of `Cage`s which contain a list of `Animal`s."

    Instances provide some useful methods to get some of the animals in the ZOO
    by a given criteria and get some metrics of the entire zoo as well as
    formatted human-readable string representation through the `str` protocol.

    Attributes:
        cages (List[Cage]): List of cages in the zoo. Should not be modified
          "by hand". Use `add_cages` method for this purpose.
    """
    cages: List[Cage] = field(default_factory=list)

    def add_cages(self, *cages):
        """Add `cages` to the end of the list of cages in the ZOO.
        """
        self.cages.extend(cages)

    def animals_by_color(self, color: str) -> List[Animal]:
        """Returns list of the animals in the ZOO of color specified by the `color`.
        """
        return [
            animal for animal in self._all_animals() if animal.color == color
        ]

    def animals_by_legs(self, number_of_legs: int) -> List[Animal]:
        """Returns list of the animals in the ZOO having `number_of_legs` legs.
        """
        return [
            animal for animal in self._all_animals()
            if animal.number_of_legs == number_of_legs
        ]

    def number_of_legs(self) -> int:
        """Returns total number of legs of all the animals in the ZOO."""
        return sum(animal.number_of_legs for animal in self._all_animals())

    def _all_animals(self) -> Generator[Animal, None, None]:
        return (animal for cage in self.cages for animal in cage.animals)

    def __str__(self) -> str:
        all_cages_str = "\n".join(str(cage) for cage in self.cages)
        return f"All cages in this zoo contain:\n{all_cages_str}"


def _main():
    wolf = Wolf('black')
    sheep = Sheep('white')
    snake = Snake('brown')
    parrot = Parrot('green')

    cage1 = Cage(1)
    cage1.add_animals(wolf, sheep)

    cage2 = Cage(2)
    cage2.add_animals(snake, parrot)
    zoo = Zoo()

    zoo.add_cages(cage1, cage2)

    print(zoo)
    print(zoo.animals_by_color('white'))
    print(zoo.animals_by_legs(4))
    print(zoo.number_of_legs())


if __name__ == "__main__":
    _main()
