"""takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.

The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
If the list contains an even number of elements, your function should return the average of the middle two.
"""

def median(arr):
  new_arr = sorted(arr)
  mid = new_arr[len(arr)/2]
  if len(arr) % 2 != 0:
    return mid
  else:
    lower_mid = new_arr[new_arr.index(mid)-1]
    return (lower_mid+mid)/2.0

print median([7, 3, 1, 4]) #3.5
print median([7, 12, 3, 1, 6])
print median([1, 34, 1, 6, 8, 0])
print median([4, 5, 5, 4]) #4.5
