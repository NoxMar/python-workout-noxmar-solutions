#!/usr/bin/env python3
"""
Solution for exercise 19 "passwd_to_dict" from chapter 5 of "Python Workout" by Reuven M. Lerner
"""

from os import PathLike


def passwd_to_dict(passwd_path: PathLike = "/etc/passwd") -> dict[int, str]:
    """Returns dict mapping uids to usernames in passwd file.

    Args:
        passwd_path (PathLike, optional): Path to file of passwd-like structure.
        Defaults to "/etc/passwd".

    Returns:
        dict: Dict mapping uids to usernames.

    Raises:
        IOError: File does not exist or you don't have or cannot be read (most
        likely due to permissions issues).
    """
    uid_uname = {}
    with open(passwd_path, encoding='utf-8') as f:
        for line in f:
            if line.startswith(("#", '\n')):
                continue
            fields = line.strip().split(':')
            uid_uname[fields[0]] = fields[2]

    return uid_uname


if __name__ == "__main__":
    print(passwd_to_dict())
