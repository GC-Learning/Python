"""Show a simple bar chart of the letters used in a sentence."""

from pprint import pprint
from collections import defaultdict

def def_value():
    """Return an empty array."""
    return []

def is_valid_letter(letter):
    """Validate a letter."""
    return letter not in [" "]

def main():
    """Asks for a sentence to show a simple bar chart."""
    sentence = input("Type a sentence: ").lower()
    letters_map = defaultdict(def_value)
    keys = "abcdefghijklmnopqrstuvwxyz"

    for key in keys:
        letters_map[key]

    for letter in sentence:
        if not is_valid_letter(letter):
            continue

        letters_map[letter].append([letter])

    pprint(letters_map)

if __name__ == "__main__":
    main()
