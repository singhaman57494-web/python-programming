#           Array/ list

marks = [88, 72, 95, 61, 79]

# access
print(marks[0])  
print(marks[2])  
print(marks[-1]) 

#  add to ending    o(1)

marks.append(100)
print(marks)  

# specific position    o(n)

marks.insert(2, 55)
print(marks)     

# o(1)     Delete

marks.pop(2)
print(marks) 

#   slicing

print(marks[1 : 3])
print(marks[::2])
