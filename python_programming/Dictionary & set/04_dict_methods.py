#                            Dictionary methods

# Create a nested dictionary
student = {
    "name": "mukul",
    "details": {
        "age": 21,
        "course": "BCA",
        "marks": {
            "java": 90,
            "python": 85,
            "math": 88,
            "dsa": 82
        }
    }
}
#   print dictionary 
print(student) 

# print total keys

print(student.keys())  #returns all keys

# print list type on key

print(list(student.keys())) 

# print length dictionary

print(len(student))


print(student.values())  # return all values
print(list(student.values()))


print(student.items())   # returns all (key , val) pairs as tuples
print(list(student.items()))   

# print(student("name2")) # error
print(student.get("name2"))  #return None value

new_dict = {"city" : "delhi", "rollno" : 25516}
student.update(new_dict)  # inserts the specified items to the dictionary

print(student)