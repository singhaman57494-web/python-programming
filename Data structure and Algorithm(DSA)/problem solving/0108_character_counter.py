#                              character counter 

def count_character(text):
    vowels = consonants = digits = spaces = 0
    for char in text:
        if char.lower()  in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isdigit():
            digits += 1
        elif char == " ":
            spaces += 1
    return "vowels : ", vowels, "consonants : ", consonants,"digits : ", digits,"spaces :", spaces

print(count_character("programming2 3 word"))