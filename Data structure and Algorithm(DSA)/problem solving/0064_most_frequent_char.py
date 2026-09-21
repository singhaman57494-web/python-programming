#                      most frequent character

text = "programming"
freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
            

print(freq)

highest = 0
most_frequent = ""

for char in freq:
    if freq[char] > highest:
        highest = freq[char]
        most_frequent = char

print(most_frequent, highest)