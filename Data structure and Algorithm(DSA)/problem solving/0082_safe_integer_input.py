#                               exception handling + user input



try: 
    num = int(input("enter a number : "))

except ValueError:
    print("Invalid input")