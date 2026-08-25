numbers = list(map(int, input("enter the numbers : ").split()))

maxium = numbers[0]

for num in numbers:
    if num > maxium:
        maxium = num

print("maxium =", maxium)
