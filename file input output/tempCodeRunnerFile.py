f = open("student.txt", "r")

data = f.read()
print(type(data))
print(data)
f.close()

line1 = f.readline()
print(line1)