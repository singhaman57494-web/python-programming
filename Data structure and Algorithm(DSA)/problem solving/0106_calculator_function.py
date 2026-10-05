#                     mini calculator

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            print("0 not divided ")
    else:
        print("wrong operator ")

print(calculator(10, 20, "+"))
print(calculator(10, 20, "-"))
print(calculator(10, 20, "*"))
print(calculator(10, 20, "/"))