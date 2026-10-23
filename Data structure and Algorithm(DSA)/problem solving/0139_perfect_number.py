#                          perfect number 

def perfect(n):
    original = n
    total = 0
    for i in range(1, n, +1):
        if n % i == 0:
            total += i

    if total == original:
        print("perfect number")
    else:
        print("not perfect")

perfect(6)
perfect(28)
perfect(12)