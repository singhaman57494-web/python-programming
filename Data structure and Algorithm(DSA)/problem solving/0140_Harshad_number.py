#                                 Harshad number
def harshad(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    
    if original % total == 0:
        print("harshad number")
    else:
        print("not harshad")

harshad(18)
harshad(12)
harshad(14)