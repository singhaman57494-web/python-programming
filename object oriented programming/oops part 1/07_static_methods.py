#                             static methods

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def get_avg():
        sum = 0
        for val in s1.marks:
            sum += val
        print("Hi student ", s1.name, "your average score is : ", sum/3)

s1 = student("prakash", [94, 44, 78])

print(s1.name, s1.marks)
s1.get_avg()