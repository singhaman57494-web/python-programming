#                       check armstrong number

def armstrong(n):
    original = n
    count = 0
    while n > 0:
        n = n // 10
        digit = n % 10
        count += 1

    n = original