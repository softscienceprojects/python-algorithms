"""takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

Assume your input strings won’t contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
"""


def censor(text, word):
  arr = text.split(" ")
  for w in arr:
    if w == word:
      arr[arr.index(w)] = "*" * len(word)
  return " ".join(arr)
