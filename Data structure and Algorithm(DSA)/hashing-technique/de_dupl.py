#                          remove duplicate  emails

signin = [
    "ravi@gmail.com",
    "priya@gmail.com",
    "ravi@gmail.com",
    "sneha@gmail.com",
    "priya@gmail.com",
    "ravi@gmail.com",
    "priya@gmail.com",
    "chirag@gmail.com",
    "sneha@gmail.com",

]

def remove_duplicate(emails):
    seen = set()
    unique = []

    for email in emails:
        if email not in seen:
            unique.append(email)
            seen.add(email)

    return unique

clean = remove_duplicate(signin)
print(clean)