# 5. Using reduce() to find the largest number
# without using max()

from functools import reduce

numbers = [12, 45, 7, 89, 34, 67]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print("Largest:", largest)