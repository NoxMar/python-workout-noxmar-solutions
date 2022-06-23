#!/usr/bin/env python3
"""
Solution for exercise 14 "restaurant" from chapter 4 of "Python Workout" by Reuven M. Lerner
"""

_MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}


def restaurant():
    """Asks user for items to add to their order displaying total afterwards.

    Source of items user can select from the menu is the dict `_MENU`. After
    user enters their input if it's found in the dict as a key price and
    total up to this point are displayed. If the user's choice is not a key in
    this dict then user is informed about that fact. On an empty input from the
    user this function will display the total and return.
    """
    total = 0
    while order := input("Order: ").strip():
        try:
            cost = _MENU[order]
        except KeyError:
            print(f"Sorry, we are fresh out of {order} today.")
            continue

        total += cost
        print(f"{order} costs {cost}, total is {total}")
    print(f"Your total is {total}")


if __name__ == "__main__":
    restaurant()
