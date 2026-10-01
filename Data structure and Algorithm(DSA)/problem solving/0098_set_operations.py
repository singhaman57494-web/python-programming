#                        set operations

python_team = {"Rahul", "Aman", "Priya", "Karan", "Neha"}

web_team = {"Aman", "Priya", "Rohit", "Vikas", "Neha"}

common = python_team & web_team
python_member = python_team - web_team
web_member = web_team - python_team
all_members = python_team | web_team
unique_member = python_team ^ web_team

print("Commom Member : ", common)
print("Only python : ", python_member)
print("Web Member  : ", web_member)
print("Unique Member : ", unique_member)
print("All Member : ", all_members)
print("Total : ", len(all_members))


