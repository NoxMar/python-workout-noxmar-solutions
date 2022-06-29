#!/usr/bin/env python3
"""
Solution for exercise 12 "most_repeating_letters" from chapter 3 of "Python Workout" by Reuven M. Lerner
"""

from typing import Sequence, Optional
from collections import Counter


def _word_to_most_common_letter_count(word: str) -> int:
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words: Sequence[str]) -> Optional[str]:
    """Returns string with maximum repetitions of its most common character.

    If `words` is empty returns `None`.

    Args:
        words (Sequence[str]): Sequence of words to choose most repeating from.

    Returns:
        Optional[str]: String with most repetitions or `None` if words is empty.
    """
    return max(words, key=_word_to_most_common_letter_count, default=None)


if __name__ == "__main__":
    words_ = ['this', 'is', 'an', 'elementary', 'test', 'example']
    print(most_repeating_word(words_))
