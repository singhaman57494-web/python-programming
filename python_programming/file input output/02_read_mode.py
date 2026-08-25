f = open("student.txt", "r")

data = f.read()
print(type(data)) # reads entire file
print(data)
f.close()

line1 = f.readline() # print line 1
print(line1)

line2 = f.readline() # print line 2
print(line2)


# data = f.read(5) // reads entire file

# data = f.readline() # read one line at a time