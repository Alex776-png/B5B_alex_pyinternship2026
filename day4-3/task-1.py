def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both values must be numbers.")


print(safe_division(10, 2))   # 5.0
safe_division(10, 0)          # Error: Cannot divide by zero.
safe_division(10, "2")        # Error: Both values must be numbers.