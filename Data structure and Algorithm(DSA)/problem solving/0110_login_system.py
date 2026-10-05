#                            simple login system

def login(username, password):
    if username == "admin" and password == "Python@123":
        return "login Successfully"
    else:
        return "your detail not match try again!"

print(login("admin", "Python@123"))