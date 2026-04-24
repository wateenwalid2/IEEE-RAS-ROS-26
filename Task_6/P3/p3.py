class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Can't continue in this operation")
    
acc = BankAccount()
acc.deposit(50)
print(f"Your balance now is {acc.balance}")
acc.withdraw(30)
print(f"Your balance now is {acc.balance}")
acc.withdraw(30)
print(f"Your balance now is {acc.balance}")
