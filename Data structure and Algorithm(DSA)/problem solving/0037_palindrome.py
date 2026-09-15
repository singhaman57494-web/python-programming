#                                     string palinfrome or not

string = "madam"
reverse = ""
for i in range(len(string)-1,-1, -1):
    reverse += string[i]

def palindrome(string, reverse):
    if reverse == string:
        return True
    else:
        return False

print(palindrome(reverse, string))
