"""takes an integer x as input.

Calculate and return the factorial of that number.
"""

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
