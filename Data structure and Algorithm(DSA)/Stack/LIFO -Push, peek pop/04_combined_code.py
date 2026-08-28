value = []

# pop = value.pop()
# print(pop)# error pop from empty list

value.append(34)
value.append(44.6)
value.append(67)
value.append(42)
value.append(76)
print(value)

# peek
print("peek item : ", value[-1])
print("After peek", value)

# pop

popped = value.pop()
print("popped value :", popped)
print(value)

pop = value.pop()
print(pop) # pop new peek value