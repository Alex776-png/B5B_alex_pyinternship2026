from datetime import date

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

birth_date = date(year, month, day)
today = date.today()

age = today.year - birth_date.year

# Subtract one if the birthday hasn't occurred yet this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Your exact age is:", age, "years")