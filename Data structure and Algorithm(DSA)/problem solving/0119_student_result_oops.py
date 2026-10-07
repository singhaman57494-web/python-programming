#                                student result system using oops 

class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
    def calculate_total(self):
        total = sum(self.marks)
        return total

    def calculate_average(self):
        Average = sum(self.marks) / len(self.marks)
        return Average

    def show_result(self):
        print("Name = ", self.name)
        print("Roll No = ", self.roll_no)
        print("Marks = ", self.marks)

        total = self.calculate_total()
        Average = self.calculate_average()
        print("Total = ", total)
        print("Average : ", Average)
        if(Average >= 40):
            print("Result : pass")
        else:
            print("Result : Fail")

student1 = student("Rakesh", 44, [46, 33, 42, 29])
student2 = student("manoj", 23, [96, 83, 85, 98])

student1.show_result()
student2.show_result()