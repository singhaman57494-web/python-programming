#                        group words by first letter

words = ["apple", "banana", "avocado", "mango", "blueberry", "apricot"]

grouped = {}

for word in words:
    if word[0] in grouped:
        grouped[word[0]].append(word)
    else:
        grouped[word[0]] = [word]

print(grouped)