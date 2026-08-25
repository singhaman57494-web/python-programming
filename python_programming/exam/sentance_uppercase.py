# Sentence — Digit, Uppercase, Lowercase Count

sentence = input("Enter a sentence: ")

digits = 0
uppercase = 0
lowercase = 0

for ch in sentence:

    if ch.isdigit():
        digits += 1

    elif ch.isupper():
        uppercase += 1

    elif ch.islower():
        lowercase += 1

print("Digits =", digits)
print("Uppercase =", uppercase)
print("Lowercase =", lowercase)