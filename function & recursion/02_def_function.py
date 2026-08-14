def calc_sum(a,b):  # parameter
    return a + b

a = 4
b = 6
print("first sum is :", calc_sum(a, b)) # arguments (a, b) # function call


a = 14
b = 34
print("second sum is : ", calc_sum(a, b))

print("third sum is : ", calc_sum(2, 24))

#                                   without parameter and without argument


def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

#                                         without return none output

def print_name():
    print("gemini")

output = print_name()
print(output)

#                                calculate average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    average =(sum/3)
    print(average)
    return average

calc_avg(4, 6, 9)
