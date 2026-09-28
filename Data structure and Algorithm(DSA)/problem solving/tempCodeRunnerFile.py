def student_profile(**keywargs):
    for name, age, course, city in keywargs.items():
        print("name : ", name,"Course : ", course)
        if age >= 18:
            print("adult student")
        else:
            print("minor student")

student_profile (
    name = "Rahul",
    age = 20,
    course = "python",
    city = "Noida"
)