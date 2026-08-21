def require_positive(function):
    def wrapper(*args, **kwargs):
        # Check positional arguments
        for value in args:
            if not isinstance(value, (int, float)) or value <= 0:
                print("Error: All arguments must be positive numbers.")
                return

        # Check keyword arguments
        for value in kwargs.values():
            if not isinstance(value, (int, float)) or value <= 0:
                print("Error: All arguments must be positive numbers.")
                return

        return function(*args, **kwargs)

    return wrapper


@require_positive
def divide(a, b):
    return a / b


print(divide(10, 2))   
print(divide(10, 0))   
print(divide(-10, 2))  