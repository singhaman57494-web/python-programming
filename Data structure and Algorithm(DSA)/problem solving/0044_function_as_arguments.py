#                                  function as arguments


x = 5

def square(x):
    return x * x

def calculate(func, number):
    return func(number)

print(calculate(square, x))


#                           part 2
y = 3
def double(x):
    return x * 2

def calculate(func, number):
    return func(number)

print(calculate(double, y))