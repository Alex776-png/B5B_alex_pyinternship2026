class NumberOutOfRangeError(Exception):
    pass

number = 21

try:
    if number < 1 or number > 10:
        raise NumberOutOfRangeError(
            "Number must be between 1 and 10."
        )

    print(f"Valid number: {number}")

except NumberOutOfRangeError as e:
    print(f"Error: {e}")