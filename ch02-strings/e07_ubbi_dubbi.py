#!/usr/bin/env python3
"""
Solution for exercise 7 "ubbi_dubbi" from chapter 2 of "Python Workout" by Reuven M. Lerner
"""

_VOWELS = "aeiou"


def ubbi_dubbi(word: str) -> str:
    """Converts lowercase string of words to its ubbi-dubii equivalent.

    Args:
        word (str): lowercase alphabetic string to be converted.

    Returns:
        str: word converted to ubbi-dubbi.
    """
    return "".join(f"ub{le}" if le in _VOWELS else le for le in word)


if __name__ == "__main__":
    word_ = input("Input lowercase word: ")
    print(f"Ubbi Dubbi equivalent of {word_} is {ubbi_dubbi(word_)}")
