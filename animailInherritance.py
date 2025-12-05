class Animal:
    def sound(self):
        return "make sound"

class Dog(Animal):
    def sound(self):
        return "bark"

class Cat(Animal):
    def sound(self):
        return "meow"

class Cow(Animal):
    def sound(self):
        return "moo"
    
dog = Dog()
cat = Cat() 
cow = Cow()
print(dog.sound())  # Output: bark
print(cat.sound())  # Output: meow
print(cow.sound())  # Output: moo