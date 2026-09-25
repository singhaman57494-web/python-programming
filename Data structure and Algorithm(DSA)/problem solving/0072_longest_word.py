#                           longest word in a sentence

text = "python make problem solving very interesting"

longest = ""
words = text.split()

for word in words:
    if (len(word) > len(longest)):
        longest = word

print(longest) 
