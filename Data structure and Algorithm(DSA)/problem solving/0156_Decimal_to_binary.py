#                                    Decimal to binary

def decimal_to_binary(n):
    binary = 0
    place = 1

    while n > 0:
        binary += (n % 2) * place
        n //= 2
        place *= 10

    return binary

print(decimal_to_binary(8))