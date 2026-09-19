# first non repeating character

text = "aabbcdde"
repeated = []
repeat = []

for char in text:
    if char not in repeated:
        repeated.append(char)
    else:
        repeat.append(char)

for char in repeated:
    if char not in repeat:
        print(char)
        break
else:
    print("No non-repeating character")