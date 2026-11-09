#                          count set bits

def count_set_bits(n):
    count = 0

    while n > 0:
        digit = n % 2
        if digit == 1:
            count += 1
        n = n // 2
    return count

print(count_set_bits(10))