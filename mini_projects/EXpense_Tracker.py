expenses = []

def add_expense():
    amount = int(input("enter the amount : "))
    category = input("enter category : ")
    description = input("enter discription : ")
    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description
    }
    expenses.append(expense)

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        for expense in expenses:
            print(expense["amount"])
            print(expense["category"])
            print(expense["description"])

def main():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit ")

    choice = int(input("enter the choice(1 - 5) : "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        print("Total Expense selected")
    elif choice == 4:
        print("Delete expense selected")
    elif choice == 5:
        print("Goodbye!")
    else:
        print("invalid choice")

main()