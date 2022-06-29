#!/usr/bin/env python3
"""
Solution for exercise 6 "pig_latin_sentence" from chapter 2 of "Python Workout" by Reuven M. Lerner
"""

from e05_pig_latin import pig_latin

_VOWELS = "aeiou"


def pl_sentence(sentence: str) -> str:
    """Converts lowercase string of words to pig latin.

    Does not support punctuation. Conversion is equivalent to applying
    `pig_latin` function to each word and concatenating them back into
    a sentence.

    Args:
        sentence (str): String of lowercase characters and spaces without
        punctuation.

    Returns:
        str: Pig latin equivalent of `sentence`.
    """
    return " ".join(pig_latin(word) for word in sentence.split())


if __name__ == "__main__":
    sentence_ = input("Input lowercase sentence without punctuation: ")
    print(f"Pig latin equivalent of this sentence is {pl_sentence(sentence_)}")
