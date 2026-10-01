#                          log analyzer

logs = [
    "INFO",
    "ERROR",
    "INFO",
    "WARNING",
    "ERROR",
    "INFO",
    "CRITICAL",
    "WARNING",
    "ERROR",
    "INFO"
]
freq = {}
for log in logs:
    if log not in freq:
        freq[log] = 1
    else:
        freq[log] += 1

only_once = []

maximum = 0
most = ""

for name, value in freq.items():
    if value == 1:
        only_once.append(name)

    if maximum < value:
        maximum = value
        most = name
    

print(freq)
print("Only once = ", only_once)
print("Most frequent = ", most,":", maximum)
