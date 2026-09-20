#                         duplicate characters

text = "programmingg"
not_dupl = []
duplicate = []

for char in text:
    if char not in not_dupl:
        not_dupl.append(char)
    else:
        if char not in duplicate:
            duplicate.append(char)

print(duplicate)