class Bird: 
    def fly(self):
        print("Bird is flying")

class squirrel(Bird):
    def fly(self):
        super().fly()
        print("squirrel is flying and eat")


s = squirrel()
s.fly()
