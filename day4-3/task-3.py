class InvalidAgeError(Exception):
    pass


def register_user(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(
            f"Invalid age: {age}. Age must be between 0 and 120."
        )

    print(f"User registered successfully with age {age}.")


register_user(25)

try:
    register_user(150)
except InvalidAgeError as e:
    print(e)