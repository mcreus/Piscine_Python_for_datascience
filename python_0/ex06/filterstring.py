"""
This script filters words from a string based on their length.
It accepts two arguments:
    - A string S containing words separated by spaces.
    - An integer N.

The program outputs a list of words from S that have a length greater than N.

Raises:
    AssertionError: If the number or type of arguments is invalid.
"""

import sys
import string
from ft_filter import ft_filter


def main():
    """
    Main function to filter words from a string based on their length.

    The program takes two arguments:
        - A string S containing words separated by spaces.
        - An integer N.
    It outputs a list of words from S that have a length greater than N.

    Raises:
        AssertionError: If the number or type of arguments is invalid.
    """
    av = sys.argv

    try:
        if len(av) != 3:
            raise AssertionError("the arguments are bad")
        try:
            nb = int(av[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        stringstr = av[1]
        cleanstr = "".join(
            c for c in stringstr
            if c not in string.punctuation and c != "\t" and c != "\n")
        words = cleanstr.split()
        result = ft_filter(lambda x: len(x) > nb, words)
        print(list(result))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
