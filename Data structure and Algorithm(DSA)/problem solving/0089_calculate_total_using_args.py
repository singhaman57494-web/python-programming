#                         practical use of args

def calculate_total(*args):
    total = 0

    for num in args:
        total += num

    return total

print("First call : ", calculate_total(12, 24, 36, 48))

print("second Call : ", calculate_total(15, 30, 20, 12, 50))