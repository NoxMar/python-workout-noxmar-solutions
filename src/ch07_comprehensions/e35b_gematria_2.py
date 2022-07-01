#!/usr/bin/env python3
"""
Solution for exercise 35b "gematria_dict" from chapter 7 of "Python Workout" by Reuven M. Lerner
"""

from typing import Iterable
from os import PathLike

from e35a_gematria_1 import get_letters_positions_dict  # pylint: disable=import-error

_GEMATRIA_VALUES_DICT = get_letters_positions_dict()
_WORDS_DICT_PATH = "words.txt"
_WORDS_BY_GEMATRIA = None


def gematria_for(word: str) -> int:
    """Calculate gematria for a given word according to the English alphabet.
    """
    return sum(_GEMATRIA_VALUES_DICT.get(letter, 0) for letter in word)


def gematria_equal_words(word: str,
                         dict_: PathLike = "words.txt") -> Iterable[str]:
    """Returns list of all words from `dict_` that have the same gematria as `word`.

    File pointed to by `dict_` should be dict style file (one word per line) and
    be readable. No caching is being performed since used dictionary can be
    quite large.

    Args:
        word (str): String which gematria equivalents should be found.
        dict_ (PathLike, optional): Path to dict-style file from which gematria
          equivalents are picked. Defaults to "words.txt".

    Returns:
        Iterable[str]: List of all words from `dict_` file that have the same
          gematria.
    """
    word_gematria = gematria_for(word)
    with open(dict_, encoding="utf-8") as f:
        return [
            line.strip() for line in f if gematria_for(line) == word_gematria
        ]


def _main():
    word = input("Please enter a word:")
    print("Words with equal gematria are:")
    print(*gematria_equal_words(word), sep="\n")


if __name__ == "__main__":
    _main()
