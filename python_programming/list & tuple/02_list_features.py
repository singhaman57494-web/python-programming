#                    list features
# this features perform int , float and string element.

name = ["rajeev", "sushant", "jack" , "rehan" , "bharat"]

print(name)

name.append("naveen") # adds one element at the end.
print(name)

name.sort() # sorts in ascending order
print(name)

name.sort(reverse = True) #sort to discending order.
print(name)

name.reverse() # reverse list
print(name)

values = [23, 44, 65, 74, 88]


values.insert(4, 77) #insert element at index
print(values)

values.remove(23) # remove first occurrence of element
print(values)

values.pop(4) # removes element at index
print(values)