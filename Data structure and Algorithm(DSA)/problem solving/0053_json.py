#                                      json

student = {
    "name" : "Aman",
    "age" : 18,
    "course" : "python"
}

#           import dictionary to json

import json

data = json.dumps(student)
print(data)

