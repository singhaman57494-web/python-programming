#                              check prime number

def prime_number(n):
    if n <= 1:
        return False

    for i in range(2, n, +1):
        if n % i == 0:
            return False
    return True 

ans = prime_number(7)
if ans:
    print("prime number")
else:
    print("not prime")