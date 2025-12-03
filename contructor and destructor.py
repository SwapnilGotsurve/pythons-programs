class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created ")

    def __del__(self):
        print(f"{self.name} destroyed")

p1 = Person("alice")
p2 = Person("bob ")  

del p1