#                       Automorphic number

def Automorphic(n):
    origianal = n
    square = origianal * origianal
    while n > 0:
        digit = n % 10
        last_digit = n // 100 
    if square == last_digit:
        print("Automorphic number")
    else:
        print("not Automorphic")

# Automorphic(6)
