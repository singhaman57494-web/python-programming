#                       first repeated character 

text = "abcdefeg"
repeated = []

for char in text:
    if char not in repeated:
        repeated.append(char)
    else:
        print(char)
        break