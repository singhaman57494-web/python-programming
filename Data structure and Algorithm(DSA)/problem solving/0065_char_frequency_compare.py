#                         character frequency comparision

text1 = "aabbcc"
text2 = "abcabc"

freq1 = {}
freq2 = {}

def freq_comparision():
    for i in text1:
        if i not in freq1:
            freq1[i] = 1
        else:
            freq1[i] += 1

    for i in text2:
        if i not in freq2:
            freq2[i] = 1
        else:
            freq2[i] += 1

    for i in freq1:
        if freq1[i] != freq2[i]:
            return False
        
    if len(freq1) != len(freq2):
        return False
        
    return True

print(freq_comparision())
    