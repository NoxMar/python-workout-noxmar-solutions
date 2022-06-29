#!/usr/bin/env python3
"""
Solutions for exercise 3 "run_timing" from chapter 1 of "Python Workout" by Reuven M. Lerner
"""


def run_timing() -> None:
    """Calculates and prints average from run times entered by the user.

    Asks user to enter additional run times until 0 or empty string are
    provided. Data as well as results use floating-point numbers. User input
    is not validated.
    """
    total_time = 0.
    run_count = 0

    while True:
        run_time = input("Enter 10 km run time: ")
        if not run_time:
            break

        run_time = float(run_time)
        if not run_time:
            break

        total_time += run_time
        run_count += 1

    print(f"Average of {total_time / run_count:.2f}, over {run_count} runs.")


if __name__ == "__main__":
    run_timing()
