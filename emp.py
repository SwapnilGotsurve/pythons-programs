class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_salary(self):
        print(f"name = {self.name} , salary = {self.salary} ")
    
    def give_raise(self , amount):
        self.salary += amount
        print(f"the increment salary = {self.salary} salary incremented by {amount}")

e1 = Employee("swapnil" , 50000)
e1.show_salary()
e1.give_raise(5000)