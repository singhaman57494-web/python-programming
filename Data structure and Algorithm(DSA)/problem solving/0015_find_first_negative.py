#                        find the first negative number in list

numbers = [5, 8, 12, -4, -9, 3]

for neg in numbers:
    if neg < 0:
        print("fist negative : ", neg)
        break