import random

numbers = [random.randint(10, 50) for _ in range(5)]

numbers.sort()

print("Sorted list:", numbers)