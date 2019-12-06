"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.
"""

import re

def alphabet_position(text):
    pos = ""
    for letter in text:
        if re.search('[0-9]', letter):
            continue
        else:
            find_pos = ord(letter.lower())-96
            if find_pos > 0:
                pos += str(find_pos) + " "
    return pos[:-1]
