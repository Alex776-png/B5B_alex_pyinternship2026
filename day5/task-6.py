class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.area() == other.area()


rectangle1 = Rectangle(4, 6)   # Area = 24
rectangle2 = Rectangle(3, 8)   # Area = 24

print("Rectangle 1 area:", rectangle1.area())
print("Rectangle 2 area:", rectangle2.area())
print("Are rectangles equal?", rectangle1 == rectangle2)