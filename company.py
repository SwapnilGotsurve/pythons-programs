class Employee:
    company = "honda"
    def __init__(self, name):
        self.name = name
        print(f"{self.name} working at {self.company}")  #1st way to access class variable
        print(f"{self.name} working at {Employee.company}") #2 way to access class variable

    def __del__(self):
        print(f"{self.name} is destroyed")
    

e1 = Employee("swapnil")
del e1
e2 = Employee("ram")