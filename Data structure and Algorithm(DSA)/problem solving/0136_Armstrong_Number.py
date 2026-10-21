#                       check armstrong number

def armstrong(n):
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
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong(153)
armstrong(154)

