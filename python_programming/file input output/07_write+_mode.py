f = open("demo.txt", "w+")  # delete file old data

print(f.read())
f.write("this is basic of python!")

f.close()