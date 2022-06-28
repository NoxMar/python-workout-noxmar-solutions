#!/usr/bin/env python3
"""
Solution for exercise 23 "test_scores" from chapter 5 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike
from typing import Optional, Iterable
from collections import defaultdict
import json
import glob


class StatTracker:
    """Provides min, max, sum and avg value without storing all of the values.

    This class provides aforementioned statistic for data points added with
    `append` or `extend` methods without storing all of the provided values.
    Those statistics are computed on each call of `append` or `extend` methods,
    properties returning those values do not perform any computation or have
    any side effects.

    Normal usage patter would include creating an instance, calling `append` or
    `extend` multiple times as the data becomes available and then checking
    results by the use of the appropriate properties at times when those
    properties are needed.

    """

    def __init__(self):
        self._count = 0
        self._sum = 0
        self._min = None
        self._max = None
        self._avg = None

    @property
    def sum(self) -> Optional[float | int]:
        """Sum of values provided up to this point."""
        return self._sum

    @property
    def min(self) -> Optional[float | int]:
        """Minimum of the value provided up to this point. If no were provided
        then it's `None`."""
        return self._min

    @property
    def max(self) -> Optional[float | int]:
        """Maximum of the value provided up to this point. If no were provided
        then it's `None`."""
        return self._max

    @property
    def avg(self) -> Optional[float]:
        """Average of the value provided up to this point. If no were provided
        then it's `None`."""
        return self._avg

    @property
    def count(self) -> int:
        """Count of the value provided up to this point."""
        return self._count

    def append(self, value: int | float) -> None:
        """Adds single data point to the tracked statistics.

        Args:
            value (int | float): Value to be added to the tracked sequence.
        """
        self._count += 1
        if self.count == 1:
            self._min = self._max = self._avg = self._sum = value
        else:
            self._min = min(self.min, value)
            self._max = max(self.max, value)
            self._sum += value
            self._avg = self.avg + ((value - self.avg) / self.count)

    def extend(self, values: Iterable[int | float]) -> None:
        """Adds all of the data points from values to the tracked statistics.

        Calling this method is equivalent to calling `append` on each element
        of the `values` iterable.

        Args:
            values (Iterable[int  |  float]): Data points to add to statistics.
        """
        for value in values:
            self.append(value)


def print_scores(scores_dir: PathLike):
    """Prints per-file per-subject score summary for JSON files in `scores_dir`.

    Compiles min, max, and average of scores per each subject from JSON files
    of a following structure:
    ```
    [
        {"subject_a": 50, "subject_b": 10, ...},
        {"subject_a": 30, "subject_b": 30, ...}
    ]
    ```
    Summary will be printed in the following format:
    ```
    <FILE_PATH_1>
        <SUBJECT_1>: min <MIN> max <MAX> average <AVG>
        ...
        <SUBJECT_N>: min <MIN> max <MAX> average <AVG>
    ...
    <FILE_PATH_N>
        <SUBJECT_1>: min <MIN> max <MAX> average <AVG>
        ...
        <SUBJECT_N>: min <MIN> max <MAX> average <AVG>
    ```
    Where `<MIN>` and `<MAX>` can be integer if all values are integers and
    floating point otherwise while `<AVG>` is always floating point with one
    decimal place.

    Args:
        scores_dir_path (PathLike): Path to the directory containing JSON files.
          Nonexistent directories would be threated as if they were empty.
    """
    stas_per_class_subject = defaultdict(lambda: defaultdict(StatTracker))

    for file_name in glob.glob(f"{scores_dir}/*.json"):
        print(file_name)
        with open(file_name, encoding="utf-8") as file:
            for scores_per_student in json.load(file):
                for subject, score in scores_per_student.items():
                    stas_per_class_subject[file_name][subject].append(score)

    for class_name, trackers in stas_per_class_subject.items():
        print(class_name)
        for subject, tracker in trackers.items():
            print(f"\t{subject}: min {tracker.min} max {tracker.max} "
                  f"average {tracker.avg:.1f}")


if __name__ == "__main__":
    print_scores("scores")
