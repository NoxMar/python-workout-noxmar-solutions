#!/usr/bin/env python3
"""
Solution for exercise 15 "rain" from chapter 4 of "Python Workout" by Reuven M. Lerner
"""


def get_rainfall():
    """Asks user for a city name and rainfall in mm and then displays totals.

    User is asked to input the city. If the input is empty this function prints
    the summary and exits. If it's not empty asks users for the integer
    amount of rain in mm and then adds it to the total for this city and asks
    for another city until empty input is provided.

    Summary is comprised of the cities being inputted at least once and the
    amount of rain recorded in them. Results are printed one per line.
    """
    city_rainfall = dict()

    while city := input("Enter city name: ").strip():
        current_rainfall = int(input("Enter mm rain: "))
        city_rainfall[city] = city_rainfall.get(city, 0) + current_rainfall

    for city, rainfall in city_rainfall.items():
        print(f"{city}: {rainfall}")


if __name__ == "__main__":
    get_rainfall()
