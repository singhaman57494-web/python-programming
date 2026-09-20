#                        anagram check

text1 = "listen"
text2 = "silent"

count = {}

for char in text1:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

def anagram():
    for char in text2:
        if char in count:
            count[char] -= 1
        else:
            return False
        
    for value in count.values():
        if value != 0:
            return False
            
    return True


print(anagram())


