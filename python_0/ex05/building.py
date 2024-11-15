"""
This is my building.py
"""

import sys
import string


def count_string(s: string):
    """
    This fonction analyzes a string and counts
    characters, upper letters, lower letters, spaces, digits, and punctuation.
    """

    characters = 0
    upperLetters = 0
    lowerLetters = 0
    punctuationMarks = 0
    spaces = 0
    digits = 0

    for c in s:
        characters += 1
        if c.isupper():
            upperLetters += 1
        elif c.islower():
            lowerLetters += 1
        elif c.isspace():
            spaces += 1
        elif c.isdigit():
            digits += 1
        else:
            punctuationMarks += 1

    print(f"The text contains {characters} characters:")
    print(f"{upperLetters} upper letters")
    print(f"{lowerLetters} lower letters")
    print(f"{punctuationMarks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Thats the main function
    """

    av = sys.argv
    try:
        if len(av) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(av) == 1:
            input_string = input("What is the text to count?\n")
            av.append(input_string)
            response = av[1]
            count_string(response)
        elif len(av) == 2:
            response = av[1]
            count_string(response)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
main()
