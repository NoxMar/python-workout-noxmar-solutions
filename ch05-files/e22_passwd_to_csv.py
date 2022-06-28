#!/usr/bin/env python3
"""
Solution for exercise 22 "passwd_to_csv" from chapter 5 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike
import csv


def passwd_to_csv(results_path: PathLike,
                  passwd_path: PathLike = "/etc/passwd"):
    """Writes usernames nad uids from passwd-like file to a CSV file.

    Resulting CSV file is delimited by tab characters and contains two columns:
    username and uid.

    Args:
        results_path (PathLike): Path of the resulting CSV file. File has to be
          writeable by the program. Intermediate directories won't be created.
        passwd_path (PathLike, optional): Path to passwd-like file from which
          data will be extracted. File needs to be readable by the program.
          Defaults to "/etc/passwd".
    """
    with open(passwd_path, encoding='utf-8') as f_passwd, open(
            results_path, 'w', encoding='utf-8') as f_results:
        passwd_reader = csv.reader(f_passwd, delimiter=':')
        results_writer = csv.writer(f_results, delimiter='\t')

        for row in passwd_reader:
            if len(row) <= 2:
                continue
            results_writer.writerow((row[0], row[2]))


if __name__ == '__main__':
    passwd_to_csv("passwd.csv")
