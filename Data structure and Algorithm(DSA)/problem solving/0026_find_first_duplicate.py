#                     find the first duplicate number in list

numbers = [4, 7, 2, 9, 7, 5, 2]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)
    else:
        print(num)
        break
    
        

        

