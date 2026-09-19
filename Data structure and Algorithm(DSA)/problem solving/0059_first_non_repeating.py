# first non repeating character

text = "aabbcdde"
unique = []
repeat = []

for char in text:
    if char not in unique:
        unique.append(char)
    else:
        repeat.append(char)

for char in unique:
    if char not in repeat:
        print(char)
        break
else:
    print("No non-repeating character")