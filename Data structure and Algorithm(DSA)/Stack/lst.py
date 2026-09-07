stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack)

print("top item : ", stack[-1])

item = stack.pop()
print(stack)

print(len(stack) == 0)