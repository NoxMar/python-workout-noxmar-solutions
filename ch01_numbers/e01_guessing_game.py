#!/usr/bin/env python3
"""
Solutions for exercise 1 from chapter 1 of "Python Workout" by Reuven M. Lerner
"""

from random import randint

_GUESS_MIN = 0
_GUESS_MAX = 100


def guessing_game():
    """Asks user to guess number from 0 to 100(inclusive) until they succeed.

    Prints feedback after each guess if your input was to low, to high or
    correct. If user's guess was correct, function exits.

    Raises:
        ValueError: User's input wasn't parsable to integer.
    """
    correct_answer = randint(_GUESS_MIN, _GUESS_MAX)

    while (guess := int(input("What is your guess? "))) != correct_answer:
        relation = "low" if guess < correct_answer else "high"
        print(f"{guess} is too {relation}.")
    print(f"Right, answer is {guess}")


if __name__ == "__main__":
    guessing_game()
