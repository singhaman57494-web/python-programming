with open("test.txt", "r") as f:
    content = f.read()
    print(content)

with open("test.txt", "w") as f: # overite
    f.write("New data")