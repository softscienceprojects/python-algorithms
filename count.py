""" has two arguments called sequence and item.

Return the number of times the item occurs in the list.

For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).

There is a list method in Python that you can use for this, but you should do it the long way for practice.
Your function should return an integer.
The item you input may be an integer, string, float, or even another list!
"""

def count(sequence, item):
  total = 0
  for n in sequence:
    if n == item:
      total += 1
  return total
