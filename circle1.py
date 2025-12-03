class Shape:
    def area(self):
        print("every shape has an area")


class Circle(Shape):
    def area(self):
        super().area()
        print("Area of circle is pi * r*r")

c = Circle()
c.area()