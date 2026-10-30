#                                   perfect number 

def perfect(n):
    original = n
    total = 0
    for i in range(1, n , +1):
        if n % i == 0:
            total += i
    if total == original:
        return True
    else:
        return False

Ans = perfect(28)

if Ans:
    print("perfect Number")
else:
    print("not perfect")
