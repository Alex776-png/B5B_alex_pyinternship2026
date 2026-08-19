class NumberOutOfRangeError(Exception):
    pass


while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))

        if number < 1 or number > 10:
            raise NumberOutOfRangeError(
                "Number must be between 1 and 10."
            )

        print(f"Valid number: {number}")
        break

    except ValueError:
        print("Error: Please enter a numeric value.")

    except NumberOutOfRangeError as e:
        print(f"Error: {e}")