#                              default function

# assigning a default value to parameter, which is used when no argument is passed.

def calc_prod(a=2,b=4):
    print(a * b)
    return a * b

calc_prod()

# type 2

def calc_prod(a,b=4):
    print(a * b)
    return a * b

calc_prod(1)