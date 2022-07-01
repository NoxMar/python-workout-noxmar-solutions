#!/usr/bin/env python3
"""
Solution for exercise 43 "animals" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class Animal(ABC):
    """Abstract animal described by species, number of legs and color.

    Instances provide formatted descriptions through the `str` protocol.

    Attributes:
        color (str): String representing the color of the animal.

    Properties:
        number_of_legs (int): Number of legs animal possesses. **This property is
          abstract and should be overridden by each subclass** according to
          animal they represent.
        species(str): Species of the animal. Class names is used by default.
    """
    color: str

    @property
    @abstractmethod
    def number_of_legs(self) -> int:
        """Number of legs the animal has."""

    @property
    def species(self) -> str:
        """String representation of the species of the animal.

        Normally name of the class is used.
        """
        return self.__class__.__name__

    def __str__(self):
        return (f"{self.color} {self.species}, "
                f"{self.number_of_legs} legs").capitalize()


@dataclass
class Wolf(Animal):
    """Animal subclass representing wolfs.

    Instances always have 4 legs and the correct name.
    """

    @property
    def number_of_legs(self):
        return 4


@dataclass
class Sheep(Animal):
    """Animal subclass representing sheep.

    Instances always have 4 legs and the correct name.
    """

    @property
    def number_of_legs(self):
        return 4


@dataclass
class Snake(Animal):
    """Animal subclass representing snakes.

    Instances always have 0 legs and the correct name.
    """

    @property
    def number_of_legs(self):
        return 0


@dataclass
class Parrot(Animal):
    """Animal subclass representing parrots.

    Instances always have 2 legs and the correct name.
    """

    @property
    def number_of_legs(self):
        return 2


if __name__ == "__main__":
    print(Wolf('black'))
    print(Sheep('white'))
    print(Snake('brown'))
    print(Parrot('green'))
