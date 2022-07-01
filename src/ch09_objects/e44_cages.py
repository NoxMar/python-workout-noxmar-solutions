#!/usr/bin/env python3
"""
Solution for exercise 44 "cages" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

from dataclasses import dataclass, field
from typing import List, Tuple

from e43_animals import Animal, Wolf, Sheep, Snake, Parrot  # disable pylint: disable=import-error


@dataclass
class Cage:
    """Cage containing a list of animals contained within and an id.

    Instances provide formatted descriptions through the `str` protocol.

    Attributes:
        id_number (int): Id number of the cage.
        animals: (List[Animal]): List of animals contained in the cage. Should
          not be modified "by hand". Use `add_animals` method for this purpose.
    """
    id_number: int
    animals: List[Animal] = field(default_factory=list)

    def add_animals(self, *animals: Tuple[Animal]):
        """Add `animals` to the end of the list of contained animals.
        """
        self.animals.extend(animals)

    def __str__(self) -> str:
        animals_str = "\n".join(f"\t{animal}" for animal in self.animals)
        return f"Cage {self.id_number}:\n{animals_str}"


def _main():
    wolf = Wolf('black')
    sheep = Sheep('white')
    snake = Snake('brown')
    parrot = Parrot('green')

    c1_ = Cage(1)
    c1_.add_animals(wolf, sheep)

    c2_ = Cage(2)
    c2_.add_animals(snake, parrot)

    print(c1_)
    print(c2_)


if __name__ == "__main__":
    _main()
