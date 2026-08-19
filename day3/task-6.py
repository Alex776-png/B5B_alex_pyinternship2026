numbers = [10, 25, 7, 40, 30, 40, 15]

largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        second_largest = largest
        largest = number
    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

print("Second largest:", second_largest)