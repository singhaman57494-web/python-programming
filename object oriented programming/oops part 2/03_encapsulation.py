#                                 encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposit ho gaye!")
        else:
            print("Invalid amount!")

# --- Usage ---
account = BankAccount(5000)


print(account.get_balance())  # Output: 5000
account.deposit(2000)         # Output: ₹2000 deposit 
print(account.get_balance())  # Output: 7000