#              find the first non repeating number

numbers = [4, 7, 4, 2, 7, 9, 2, 5]


for num in numbers:
    count = 0

    for j in numbers:
        if num == j:
            count += 1
            
    if count == 1:
        print(num)
        break        

#              shortcut

freq = numbers.count(num)
if freq == 1:
    print(num)