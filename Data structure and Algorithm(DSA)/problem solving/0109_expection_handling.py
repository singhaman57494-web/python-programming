#                    exception handling

def divide_numbers(a, b):
    try:
        print("divided : ",a / b)
    except ZeroDivisionError:
       print("number is 0")

divide_numbers(20, 5)
divide_numbers(20, -2)
divide_numbers(20, 0)
