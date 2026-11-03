#                                     convert binary to decimal

def binary_to_decimal(n):
    decimal = 0
    power = 0
    while n > 0:
        digit = n % 10
        decimal += digit * (2 ** power)
        n = n // 10
        power += 1
    return decimal

print("binary to decimal : ", binary_to_decimal(1010))
