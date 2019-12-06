"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
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
