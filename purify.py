"""takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
"""

def purify(nums):
  result = []
  for n in nums:
    if n % 2 == 0:
      result.append(n)
  return result
