import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2

print("Dice 1:", dice1)
print("Dice 2:", dice2)
print("Sum:", total)

if total == 7 or total == 11:
    print("You Win!")
else:
    print("Try Again!")