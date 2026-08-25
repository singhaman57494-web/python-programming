import calculator
num = int(input("enter your choice(1 | 2) : "))
if num == 1:
    choice = int(input("enter your choice(1-4) : "))
    if num == 1:
        num1 = int(input("enter first number : "))
        num2 = int(input("enter second number : "))
    
        if choice == 1:
            print("result:", calculator.add(num1, num2))
        elif choice == 2:
            print("result :", calculator.subtract(num1, num2))
        elif choice == 3:
            print("result :", calculator.multiply(num1 , num2))
        elif choice == 4:
            print("result :", calculator.divide(num1 , num2))
        else:
            print("Envalid choice")

elif num == 2:
    character = input("enter the choice(Square | Cube) :")
    n = int(input("enter n number : "))
    if character == "Square":
        print("result :", calculator.square(n))
    elif character == "Cube":
        print("result :", calculator.cube(n))
else:
    print("Invalid choice..")


