#                                       safe division with exception handling

a = 20
b = 0

try:
    print("result:", a / b)

except ZeroDivisionError:
    print("cannot divided by zero")