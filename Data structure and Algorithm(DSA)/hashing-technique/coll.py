#            collision

import hashlib

hashlib.sha256("ravi@gmain.com".encode()).hexdigest()

users = {}

# insert

users["ravi@gmain.com"] = "Ravi sharma"
users["priya@gmail.com"] = "Priya patel"
users["chirag@gmail.com"] = "chirag"

print(hash("ravi@gmail.com"))
print(hash("priya@gmail.com"))
print(hash("ravi@gmail.com"))