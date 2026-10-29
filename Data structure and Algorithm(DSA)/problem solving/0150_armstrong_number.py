#                                 check Armstrong number

def is_armstrong(n):
    original = n
    count = 0
    while n > 0:
        digit = n % 10
        count += 1
        n = n // 10

    n = original
    total = 0
    while n > 0:
        digit = n % 10
        power = digit ** count
        total += power 
        n = n // 10
    if total == original:
        print("Armstrong number")
    else:
        print("not Armstrong")

is_armstrong(153)
