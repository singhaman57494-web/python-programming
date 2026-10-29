#                                          palindrome number

def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 +(digit)
        n = n // 10
    if original == reverse:
        return True
    else:
        return False

ans = is_palindrome(121)
if ans:
    print("number is palindrome")
else:
    print("number isn't palindrome")
    