#                       GCD(greatest common Divisor)

def gcd(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            common = i
    return common
    
print("common : ", gcd(12, 18))
print("common : ", gcd(20, 30))