#                         word frequency analyzer

text = "python is easy and python is powerful and easy"
frequency = {}
words = text.split()

for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

# print(frequency)

most_repeated = ""
highest_frequency = 0
for freq in frequency:
    if frequency[freq] > highest_frequency:
        highest_frequency = frequency[word]
        most_repeated = freq

print("Most frequent word : ", most_repeated)
print("Frequency : ", highest_frequency)
