#                           json to python 

data = '{"name" : "Aman", "age" : 18, "course" : "python"}'

import json

student = json.loads(data)

print(student["name"])
print(student["age"])
print(student["course"])