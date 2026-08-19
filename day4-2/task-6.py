def make_validator(min_value):
    def validate(number):
        return number >= min_value

    return validate


validator_10 = make_validator(10)
validator_50 = make_validator(50)

print("10 validator:")
print(validator_10(5))
print(validator_10(10))
print(validator_10(15))

print("\n50 validator:")
print(validator_50(25))
print(validator_50(50))
print(validator_50(75))