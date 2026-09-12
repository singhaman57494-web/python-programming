#                find the maxium number in list 

numbers = [10, 25, 7, 40, 15]
max_number = 0

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

#                           using built-in functon


print(max(numbers))

        
