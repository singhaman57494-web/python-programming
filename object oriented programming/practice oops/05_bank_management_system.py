from abc import ABC, abstractmethod

class bank(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class savingsAccount(bank):
    def __init__(self, Account_Holder, balance, interest_rate):
        self.account_Holder = Account_Holder
        self.__balance = balance
        self.interest_rate = interest_rate

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if(amount > 0):
             self.__balance += amount
             print(f"{amount} diposit your account")

    def calculate_interest(self):
        interest = (self.__balance * self.interest_rate)/100
        print(f"Total interest:{interest} INR")


acc1 = savingsAccount("Aman", 10000, 5)

print("initial balance :", acc1.get_balance())

acc1.deposit(5000)

print("updated balance :", acc1.get_balance())

acc1.calculate_interest()