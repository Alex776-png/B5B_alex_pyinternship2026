import sys

if len(sys.argv) != 4:
    print("Error: Please provide a number, an operator (+ or -), and another number.")
    print("Usage: python calculator.py 5 + 3")
    sys.exit()

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
else:
    print("Error: Operator must be + or -.")
    sys.exit()

print(result)
