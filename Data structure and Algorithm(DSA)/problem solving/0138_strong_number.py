#                                     strong number

def strong(n):
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

strong(145)        
strong(123)
strong(40585)