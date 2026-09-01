#                                    string reverse using stack (LIFO)

class stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            return None

        return self.items.pop()

# reverse function

def reverse_string(text):
    s = stack()

    # push all characters into stack
    for char in text:
        s.push(char)

    reversed_text = ""

    # pop all character in join them
    while len(s.items) > 0:
        reversed_text += s.pop()

    return reversed_text

Name = "AMAN"
result = reverse_string(Name)

print("original name : ", (Name))
print("Reversed name : ", result)

original = "semester 3 student"

result = reverse_string(original)

print("length of original : ", len(original))  # total lenth of string

print("original data : ", original)
print("reverse data : ", result)

