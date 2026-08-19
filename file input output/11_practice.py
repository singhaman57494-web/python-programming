with open("practice.txt", "w") as f:
    f.write("hi everyone! \nWe are learning file I/O. \n")
    f.write("using java.\nI like programming in java.")

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)