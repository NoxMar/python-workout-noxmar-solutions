#!/usr/bin/env python3
"""
Solution for exercise 24 "reverse_lines" from chapter 5 of "Python Workout" by Reuven M. Lerner
"""

import os
import sys


def reverse_lines(input_path: os.PathLike, output_path: os.PathLike) -> None:
    """Reverses lines form `input_path` file and writes them to `output_path`.

    Characters in line are reversed. Lines stay in the same order. `input_path`
    file must exits and program has to have appropriate permissions,
    `output_path` may or may not exist. If it does it will be overridden. Line
    endings in output file always be `\n` (UNIX-style). Input file can have
    any string of `\n` and `\r` as its line delimiter.

    Args:
        input_path (PathLike): Path to the input file.
        output_path (PathLike): Path to file to write output lines to.
    """
    with open(input_path, encoding='utf-8') as infile:
        with open(output_path, "w", encoding='utf-8') as outfile:
            for line in infile:
                line = line.rstrip('\r\n')[::-1]
                outfile.write(line)
                outfile.write('\n')


if __name__ == '__main__':
    reverse_lines(sys.argv[1], sys.argv[2])
