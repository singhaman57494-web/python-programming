#                         practice question in python

# question 1 :- create student class that takes name & marks of 3 subjects as arguements in constructor. than create a method to print the average.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        print("Hi student", self.name, "your average score is:", average)

s1 = student("prakash", [94, 44, 78])
s2 = student("kuldeep", [92, 64, 75])
s3 = student("ankit", [62, 48, 82])

print(s1.name, s1.marks)
print(s2.name, s2.marks)
print(s3.name, s3.marks)

s1.get_avg()
s2.get_avg()
s3.get_avg()