#                 same direction 

def clean(names):
    if not names:
        return 0

    left = 0
    for right in range(len(names)):
        if names[right] != names[left]:
            left = left + 1
            names[left] = names[right]

    return left + 1

names = ["Aman", "Aman", "bhavna", "chirag", "chirag", "diya"]

count = clean(names)
print(names[: count])

