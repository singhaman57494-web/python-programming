#                       move all zeroes to the end

numbers = [0, 5, 0, 3, 8, 0, 2]
count = 0
new_list = []

for num in numbers:
    if num != 0:
        new_list.append(num)

for i in numbers:
    if i == 0:
        new_list.append(i)

print(new_list)
# print(count)

#                   shortcut

numbers.sort()
print(numbers)