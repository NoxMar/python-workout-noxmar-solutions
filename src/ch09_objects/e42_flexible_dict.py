#!/usr/bin/env python3
"""
Solution for exercise 42 "flexible_dict" from chapter 8 of "Python Workout" by Reuven M. Lerner
"""


class FlexibleDict(dict):
    """Mapping checking int and string representations of a key during lookup.

    Lookups are formed in the following order:
    - original key (result of `dict[key]`)
    - string representation of a key (result of `dict[str(key)]`)
    - integer representation of a key (result of `dict[int(key)]`)

    If any of those conversions fails corresponding lookup is not performed,
    however no error is thrown. Lookup throws `KeyError` only after all of the
    listed lookup methods fail. Otherwise equivalent to built-in `dict`.
    """

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            pass
        try:
            return super().__getitem__(str(key))
        except KeyError:
            pass
        try:
            return super().__getitem__(int(key))
        except (KeyError, ValueError):
            pass
        raise KeyError(f"Neither `{key}` nor its string or int representations"
                       " are keys in this dictionary,")


def _main():
    flexible_dict = FlexibleDict()

    flexible_dict['a'] = 100
    print(flexible_dict['a'])

    flexible_dict[5] = 500
    print(flexible_dict[5])

    flexible_dict[1] = 100
    print(flexible_dict['1'])

    flexible_dict['1'] = 100
    print(flexible_dict[1])


if __name__ == "__main__":
    _main()
