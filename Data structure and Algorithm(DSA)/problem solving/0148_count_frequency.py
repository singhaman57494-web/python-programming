#                                        count frequency

text = "hello"

def frequency(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    return freq

print(frequency(text))