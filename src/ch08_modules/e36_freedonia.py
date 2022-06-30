#!/usr/bin/env python3
"""
Solution for exercise 36 "freedonia" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""

_BASE_RATES = {"Chico": 0.5, "Groucho": 0.7, "Harpo": 0.5, "Zeppo": 0.4}


def time_percentage(hour: int | float) -> float:
    """Calculates the rate by which the base state rate should be multiplied."

    This is proportional to the hour in a day as in `hour/24`.
    """
    return hour / 24


def calculate_tax(price: int | float, state: str, hour: int) -> float:
    """Calculates full amount to be paid with tax in Freedonia.

    The following formula is used to calculate the full amount:
    `price + (price * BASE_RATE_IN_STATE * hour/24)`.

    Args:
        price (int | float): Base price of the purchase (without tax).
        state (str): State in which the sale took place. Possibles values are:
          `"Chico"`, `"Groucho"`, `"Harpo"`, `"Zeppo"`
        hour (int): Full hour at which the purchase took place.

    Returns:
        float: Full price with tax.
    """
    return price + (price * _BASE_RATES[state] * time_percentage(hour))
