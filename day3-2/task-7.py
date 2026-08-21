def fun_frozenset(items):
    return frozenset(items)

numbers = [1, 2, 3, 2, 4, 1]
result = fun_frozenset(numbers)

print("Frozenset :", result)