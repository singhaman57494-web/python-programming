#                               instance methods

class bankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return amount, "deposit successfully"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount ,"withdrawal successfully"
        else:
            return "insufficient balance"

account1 = bankAccount("Rahul", 5000)
print(account1.deposit(500))
print(account1.withdraw(500))
print("total balance : ", account1.balance)