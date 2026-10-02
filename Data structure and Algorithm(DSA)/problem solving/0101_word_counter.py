#                         word counter

sentence = "python is easy and python is powerful"
freq = {}
words = sentence.split()
for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

print(freq)
maximum = 0
key = ""
for name, count in freq.items():
    if count > maximum:
        maximum = count
        key = name

print("max_freq : ", key, maximum)