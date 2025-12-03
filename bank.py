class Bank :
    def __init__(self, name , bal):
        self.name = name 
        self.bal = bal 
    
    def deposit(self, amount):
        self.bal += amount
        print(f"Deposited {amount}. New balance: {self.bal}")

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f"Withdrew {amount}. New balance: {self.bal}")
        else:
            print("Insufficient balance")

c1 = Bank("swapnil", 1000)
c1.deposit(500)
c1.withdraw(300)