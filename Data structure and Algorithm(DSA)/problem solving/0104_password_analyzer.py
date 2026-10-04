#                          function + string + loops using password analyzer


def analyze_password(password):
    has_length = False
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) >= 8:
        has_length = True

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    print("Length:", has_length)
    print("Uppercase:", has_upper)
    print("Lowercase:", has_lower)
    print("Digit:", has_digit)

    if has_upper and has_lower and has_digit and has_length:
        print("strong password")
    else:
        print("Weak password")

analyze_password("Aman@123")
