"""takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!". Don’t count Y as a vowel. 
Make sure to remove lowercase and uppercase vowels.
"""

vowels = ['a', 'e', 'i', 'o', 'u']

def anti_vowel(text):
  #returns text with all vowels removed
  no_vowels = []
  for letter in text:
    if letter.lower() not in vowels:
      no_vowels.append(letter)
  return "".join(no_vowels)
  
anti_vowel("Erin")
