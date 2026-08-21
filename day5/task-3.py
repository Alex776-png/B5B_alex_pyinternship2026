import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(21)

print("Circle area:", circle.area)
print("Circle circumference:", circle.circumference)