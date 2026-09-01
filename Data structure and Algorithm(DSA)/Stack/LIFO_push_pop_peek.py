#                    push pop peek method using stack

stack = []

# 1 Push (give 3 value)

stack.append(94)
stack.append(78)
stack.append(83)
stack.append(43)

print("all value in stack : ", stack)

#2. peek (peek operation in stack)

top_item = stack[-1]
print("top item of list : ", top_item)

#3. pop(last value pop)

item = stack.pop()
print("popped item : ", item)

# print stack after pop last value

print("stack after popped :", stack)