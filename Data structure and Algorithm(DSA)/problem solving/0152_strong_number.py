#                                  strong number

def is_strong(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        fact = 1
        while digit > 0:
            fact *= digit
            digit -= 1
        total += fact 
        n = n // 10
    if total == original:
        print("strong number")
    else:
        print("not strong")

is_strong(145)        