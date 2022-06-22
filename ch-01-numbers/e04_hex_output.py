#!/usr/bin/env python3
"""
Solutions for exercise 4 "hex_output" from chapter 1 of "Python Workout" by Reuven M. Lerner
"""

from functools import reduce


def _from_hex(hex_number: str) -> int:
    """Converts hexadecimal representation of a number to int.

    Args:
        hex_number (str): Hexadecimal number, case insensitive.

    Returns:
        int: Conversion result.
    """
    digits = (int(h, 16) for h in hex_number)
    return reduce(lambda number, d: (number << 4) + d, digits, 0)


def hex_output() -> int:
    """Asks user for hex number and prints result of its conversion to decimal.
    """
    hex_number = input("Input hex number?: ")
    number = _from_hex(hex_number)
    print(f"Hex number {hex_number} equals {number}.")


if __name__ == '__main__':
    hex_output()
