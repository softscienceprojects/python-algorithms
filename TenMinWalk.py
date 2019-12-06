"""
You always walk only a single block in a direction and you know it takes 
you one minute to traverse one city block, so create a function that will 
return true if the walk the app gives you will take you exactly ten minutes 
(you don't want to be early or late!) and will, of course, return you to your 
starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment 
of direction letters ('n', 's', 'e', or 'w' only). It will never give you 
an empty array (that's not a walk, that's standing still!).
"""


def high_and_low(numbers):
    numbers = numbers.split()
    arr = []
    for number in numbers:
        number = int(number)
        arr.append(number)
    max_and_min = sorted(arr, reverse=True)
    max_and_min = str(max_and_min[0])+" "+str(max_and_min[len(max_and_min)-1])
    return max_and_min
