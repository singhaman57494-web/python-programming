try:
    num1 = int(input("Enter number : "))
    num2 = int(input("Enter number : "))
    add = num1 + num2

except NameError:
    print("Error: fix variable name")

except ValueError:
    print("Error: enter integer value :")

except Exception as a:
    print("other error : ", a)

else:
    print("good work")

finally:
    print("nice try")