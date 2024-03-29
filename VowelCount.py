"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
"""

def getCount(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    for i in inputStr:
      if i in vowels:
        num_vowels += 1
    return num_vowels
