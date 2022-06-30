#!/usr/bin/env python3
"""
Solution for exercise 37 "menu" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

from typing import Mapping, Callable, TypeVar

T = TypeVar("T")


def menu(**options: Mapping[str, Callable[[], T]]) -> T:
    """Asks user to choose a name of the callable and returns its return value.

    Names of the named attributes are threated as "the names" and the values
    are callables (that take no argument) that will be executed. User will be
    asked to enter their choice util they chose a valid option. Name matching
    is case insensitive.

    Returns:
        T: Return value from calling the callable selected by the user.
    """
    options_choice_str = "/".join(options)
    while True:
        choice = input(f"Enter your choice (out of {options_choice_str}): ")
        try:
            return options[choice.lower().strip()]()
        except KeyError:
            print("Sorry, this is not a valid option. Please try again.")


if __name__ == "__main__":
    print("You've chosen:", menu(a=lambda: "A", b=lambda: "B"))
