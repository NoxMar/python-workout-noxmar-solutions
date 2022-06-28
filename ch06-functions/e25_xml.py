#!/usr/bin/env python3
"""
Solution for exercise 25 "xml" from chapter 6 of "Python Workout" by Reuven M. Lerner
"""


def myxml(tag: str, contents: str = "", **attributes: dict) -> str:
    """Creates XML tag (as a str) with specified name, contents, and attributes.

    Tag always consists of at least opening and  closing tags even when
    cotenants are empty. If contents are not provided then tag with empty
    contents is returned. Returned string will be of the following format:
    ```
    "<tag[ attr_k1=attr_v1, attr_k2=attr_v2, ...]]>contents</tag>"
    ```

    Args:
        tag (str): Name of the generated tag.
        contents (str, optional): Contents of the generated tag. Defaults to "".
        **attributes: Attributes of the generated tag where keys are used as
          attribute names and values are used as attribute value.

    Returns:
        str: String containing generated tag. Format explained before.
    """
    attributes_str = "".join(f" {k}=\"{v}\"" for k, v in attributes.items())
    return f"<{tag}{attributes_str}>{contents}</{tag}>"


if __name__ == "__main__":
    print(myxml("foo"))
    print(myxml("foo", "bar"))
    print(myxml("foo", "bar", a=1, b=2, c=3))
