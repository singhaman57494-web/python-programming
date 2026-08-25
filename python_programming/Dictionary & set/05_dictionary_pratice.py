#                           practice question Dictionary

# store following word meanings in a python dictionary:

dictionary = {
    "table " : ["a peace of furniture", "list of facts & figure"],
    "cat" : "a small animal"
}

print(dictionary)

#                                      set practice


#question 2:- you are given a list of subjects for students. assume one classroom is required for 1 subject. haw many classroom are needed by all students.

subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print(subjects)


# question 3 :- WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. use subject name as key & marks as value.

marks = {}

chem = int(input("enter the chem marks : "))
marks.update({"chemestery" : chem})

math = int(input("enter the math marks : "))
marks.update({"mathemetics" : math})

phys = int(input("enter the physics marks : "))
marks.update({"physics" : phys})

print(marks)


# question 4 :- figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built-in data type) 

values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)

#                         second posible solution

nums = {'9', 9.0}
print(nums)