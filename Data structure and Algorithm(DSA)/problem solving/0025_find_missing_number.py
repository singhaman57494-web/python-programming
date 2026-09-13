#                         find missing number in list 

numbers = [1, 2, 3, 5, 6, 7]
total = 0

for num in numbers:
    total += num
sum_number = 0

for i in range(1, 8):
    sum_number += i

missing =  sum_number - total
print("missing number is : ", missing)

#                     shortcut

print("missting : ", sum(range(1, 8)) - total)