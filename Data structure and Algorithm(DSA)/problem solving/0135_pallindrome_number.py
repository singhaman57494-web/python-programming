#                            palindrome number check

def palindrome(n):
    last_digit = n % 10
    reverse = n // 10
    if n == reverse:
        print("palindrome")
    else:
        print("not palindrome")

print("The number is ", palindrome(12321))