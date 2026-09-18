expenses = {
    "Travel" : {
        "Auto" : 50,
        "cab" : 200,
        "bike" : 100,
        "scooty" : 80,
        "Bus" : 40,
        "truck" : 500,
    },

    "Food" : {
        "pizza" : 250,
        "burger" : 120,
        "Biryani" : 200,
        "Momos" : 100,
        "sandwich" : 80,
    },

    "Shopping" : {
        "clothes" : 500,
        "shoes" : 1000,
        "Books" : 300
    }
}

selected_expenses = []

def add_expense():
    amount = int(input("enter the amount : "))
    category = input("enter category : ")
    description = input("enter discription : ")
    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description
    }
    selected_expenses.append(expense)

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        count = 1
        for expense in expenses:
            print(count, ".",expense["category"], "-",expense["description"],"-", "₹", expense["amount"])
            count += 1

def view_selected_expenses():
    if len(selected_expenses) == 0:
        print("No selected expenses")
    else:
        count = 1
        for expense in selected_expenses:
             print(count, ".", expense["category"],"-",expense["description"],"-", "₹",expense["amount"])
             count += 1
def total_expense():
    if len(selected_expenses)  == 0:
        print(" 0 ")
    else:
        total = 0
        for expense in selected_expenses:
            total += expense["amount"]
        print("total expenses : ", total)

def delete_expense():
    number =  int(input("enter the expense : "))
    if 1 <= number <= len(selected_expenses):
        selected_expenses.pop(number - 1)
    else:
        print("invalid expense number")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Exit ")
        print("6. view selected expenses")

        choice = int(input("enter the choice(1 - 6) : "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            total_expense()
        elif choice == 4:
            delete_expense()
        elif choice == 5:
            print("Goodbye!")
            break
        elif choice == 6:
            view_selected_expenses()
        else:
            print("invalid choice")

main()