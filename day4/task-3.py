celsius = [-12, 10, 21, 30, 39]

fahrenheit = list(
    map(lambda c: (c * 9/5) + 32, celsius)
)

print(fahrenheit)