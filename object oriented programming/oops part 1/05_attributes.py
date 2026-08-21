#                    class & object attributes

class student:
    collage_name = "abc collage"
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

s1 = student("curren", 97)
print(s1.name, s1.marks)

s2 = student("monkey", 92)
print(s2.name, s2.marks)

print(student.collage_name)