#                   Harshad number

def harshad(n):
    if n == 0:
        return False
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    if original % total == 0:
        return True
    else:
        return False
    
result = harshad(21)

if result:
    print("harshad number")
else:
    print("not harshad number ")


    
