#                                  create student profile using **keywargs


def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
    print("===================STUDENT=DETAILS=====================")
    print("name : ", kwargs["name"])
    if kwargs["age"] >= 18:
        print("adult student")
    else:
        print("minor student")
    print("course = ", kwargs["course"])
    print("city = ", kwargs["city"])

student_profile (
    name = "Rahul",
    age = 20,
    course = "python",
    city = "Noida"
)