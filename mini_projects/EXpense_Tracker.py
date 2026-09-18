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
    print("choose Category : ")

    count = 1
    for category in expenses:
        print(count, "." , category)
        count += 1

    try:
        choice = int(input("enter category : "))
        categories = list(expenses.keys())

        if 1 <= choice <= len(categories):
            category = categories[choice - 1]
            print("Selected : ", category)

            print("choose Item :")
            count = 1

            for item in expenses[category]:
                print(count, ".", item, "-", "₹", expenses[category][item])
                count += 1

            items = list(expenses[category].keys())

            try:
                item_choice = int(input("enter item : "))
                if 1 <= item_choice <= len(items):
                    item = items[item_choice - 1]
                    print("selected : ", item)

                    amount = expenses[category][item]
                    print("Amount : ", amount)

                    expense = {
                        "category": category,
                        "item": item,
                        "amount": amount
                    }
                    selected_expenses.append(expense)
                else:
                    print("invalid item")
            except ValueError:
                print("Invalid item input, try again")
        else:
            print("Invalid category")
    except ValueError:
        print("Invalid category input, try again")
    

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        for category in expenses:
            print(category)
            count = 1

            for item in expenses[category]:
                print(count , item, expenses[category][item])
                count += 1

def view_selected_expenses():
    if len(selected_expenses) == 0:
        print("No selected expenses")
    else:
        count = 1
        for expense in selected_expenses:
             print(count, ".", expense["category"],"-",expense["item"],"-", "₹",expense["amount"])
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
    try:
        number = int(input("enter the expense : "))
        if 1 <= number <= len(selected_expenses):
            selected_expenses.pop(number - 1)
        else:
            print("invalid expense number")
    except ValueError:
        print("Invalid expense input, try again")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Exit ")
        print("6. view selected expenses")

        try:
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
        except ValueError:
            print("Invalid input, try again")

main()