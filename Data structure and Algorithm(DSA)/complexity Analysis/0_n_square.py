#       --o(n^2)

def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True

numbers = [11, 22, 35, 35, 48]
result = find_duplicates(numbers)

if result:
    print("duplicate found")
else:
    print("not found")