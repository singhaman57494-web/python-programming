#                            count character frequency

character = "python"
python = {}
count = 0

for i in character:
    if i in python:
        python[i] += 1 
    else:
        python[i] = 1

print(python)


#                                  shortcut

from collections import Counter

print(Counter(character))