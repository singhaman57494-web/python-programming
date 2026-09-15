#                                         local vs global scope

x = 10   #  global variable 

def test():
    print(x)
    y = 20                 # local variable
    print(y)

test()

print(x)
