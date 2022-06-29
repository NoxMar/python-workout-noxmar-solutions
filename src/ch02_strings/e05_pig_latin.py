#!/usr/bin/env python3
"""
Solution for exercise 5 "pig_latin" from chapter 2 of "Python Workout" by Reuven M. Lerner
"""

_VOWELS = "aeiou"


def pig_latin(word: str) -> str:
    """Converts single word to its pig latin equivalent.

    Args:
        word (str): Single **lowercase** english word.

    Returns:
        str: Pig latin equivalent of `word`.
    """

    if not word:
        return ""

    return f"{word}way" if word[0] in _VOWELS else f"{word[1:]}{word[0]}ay"


def main() -> None:  #  pylint: disable=missing-function-docstring
    word = input("Input word: ")
    print(f"Pig latin equivalent of {word} is {pig_latin(word)}")


if __name__ == "__main__":
    main()
