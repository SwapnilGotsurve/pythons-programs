class Circle:
    pi = 3.14159        
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        
        return Circle.pi * (self.radius ** 2)

 
    
c1 = Circle(5)
print("Area:", c1.area())




