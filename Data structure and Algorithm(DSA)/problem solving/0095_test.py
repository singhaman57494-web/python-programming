#                           password strength checker

password = "Python@123"

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True

    if char.islower():
        has_lower = True

    if char.isdigit():
        has_digit = True

    if char == "@" or char == "#":
        has_special = True

if has_upper and has_lower and has_digit and has_special:
    print("strong password")
else:
    print("weak password")