#                                    Recursion

# when a function calls itself repeatedly.

# prints n to 1 backwords.

#                        recursive function

n = int(input("enter n number : "))

def show(n):
    if(n == 0): # Base Case
        return
    print(n)
    show(n-1)

show(n)

# second example recursion

n = int(input("enter n number : "))

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(n))

