#                        palindrome checker

def is_palindrome(text):
    original = text
    reverse = text[:: -1]
    if(original == reverse):
        return "palindrome"
    else:
        return "not palindrome"

print("The text is :", is_palindrome("madam"))
