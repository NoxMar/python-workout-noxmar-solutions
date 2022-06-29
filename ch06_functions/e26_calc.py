#!/usr/bin/env python3
"""
Solution for exercise 26 "calc" from chapter 6 of "Python Workout" by Reuven M. Lerner
"""

import operator

_operator_to_func = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "\\": operator.truediv,
    "%": operator.mod,
    "**": operator.pow
}


def calc(prefix_expr: str) -> float:
    """Computes simple (one operator two arguments) prefix notation expression.

    Supported operators are `+`, `-`, `*`, `\\`, `%`, `**` with effect equivalent
    to their ordinary effect in Python. Values for arguments fill **always**
    threated as floating point numbers. Operator and each of it's arguments need
    to be delimited by at least one character as show in examples below
    Examples:
    ```
    calc("+ 100 0.5")
    >>> 100.5
    calc("\\ 100 200")
    >>> 0.5
    ```

    Args:
        prefix_expr (str): String containing prefix notation expression with
          aforementioned limitations

    Returns:
        float: Result of computing `prefix_expr` according to prefix notation.
    """
    operator_, arg1, arg2 = prefix_expr.split()
    arg1, arg2 = float(arg1), float(arg2)

    return _operator_to_func[operator_](arg1, arg2)


if __name__ == "__main__":
    expr = input("Input one operator prefix notation expression:")
    print(calc(expr))
