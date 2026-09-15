#                              *args 

def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(10, 20))
print(add(10, 20, 30, 40, 50, 60, 70))
print(add(10, 20, 60, 70))
print(add(10, 40, 50, 60, 70))
print(add(10, 20, 40, 60, 70))
