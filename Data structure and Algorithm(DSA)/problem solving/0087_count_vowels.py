words = ['python','developer', 'programming', 'code']

result ={}

for word in words:
    count = 0

    for char in word:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    result[word] = count

print(result)