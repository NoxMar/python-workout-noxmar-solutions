#!/usr/bin/env python3
"""
Solution for exercise 8 "sort string" from chapter 2 of "Python Workout" by Reuven M. Lerner
"""


def strsort(s: str) -> str:
    """Returns string sorted by unicode character codes.

    This ordering for english letters is equivalent to alphabetic ordering.

    Args:
        s (str): String to be sorted.

    Returns:
        str: `s` sorted by UTF-8 character codes.
    """
    return "".join(sorted(s))


if __name__ == "__main__":
    str_ = input("Input a string to be sorted: ")
    print(f"{str_} sorted is: {strsort(str_)}")
