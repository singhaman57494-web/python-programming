#                           Reverse number

def reverse(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse

print(reverse(1234))