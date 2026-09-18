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

        item_choice = int(input("enter item : "))
        if 1 <= item_choice <= len(items):
            item = items[item_choice - 1]
            print("selected : ", item)

            amount = expenses[category][item]
            print("Amount : ", amount)

            expense = {
                "Category" : category,
                "item" : item,
                "Amount" : amount
            }
            selected_expenses.append(expense)

        else:
            print("Invalid category")
    
    
add_expense()
    