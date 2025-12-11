import math

# Parent class
class Shape:
    def get_perimeter(self):
        return 0

    def get_area(self):
        return 0


# Subclass of Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Override get_perimeter
    def get_perimeter(self):
        return 2 * math.pi * self.radius

    # Override get_area
    def get_area(self):
        return math.pi * self.radius * self.radius


# Create object of Circle
c = Circle(5)

print("Perimeter of Circle:", c.get_perimeter())
print("Area of Circle:", c.get_area())
