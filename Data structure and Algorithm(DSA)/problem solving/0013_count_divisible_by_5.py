#                     divisible by 5

numbers = [10, 12, 15, 7, 20, 23, 30]
count = 0

for num in numbers:
    if num % 5 == 0:
        count += 1

print("number divisible by 5 : ", count)