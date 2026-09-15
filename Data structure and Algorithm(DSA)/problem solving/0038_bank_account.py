#                                     create bank account using python class

class bankaccount:
    def __init__(self, accountholder, balance):
        self.AccountHolder = accountholder
        self.balance = balance

    def deposit(self, amount):
        self.balance +=  amount

    def withdraw(self, amount):
        self.balance -= amount

    def checkbalance(self):
        return self.balance

account = bankaccount("aman", 1000)

print("current balance is : ", account.checkbalance())
account.deposit(50)
print("current balance is : ", account.checkbalance())
account.withdraw(300)
print("current balance is : ", account.checkbalance())