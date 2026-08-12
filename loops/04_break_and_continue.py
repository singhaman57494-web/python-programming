#                                              break

# used to terminate the loop when encountered.

n = 6
i = 1

while i < 10:
    print(i)
    if i == n:
        break # find value and break loop 
    i += 1

#                                            continue

# terminates execution in the current iteration & continues execution of the loop with the next iteration.

i = 1
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue  # skip 
    print(i)
    i += 1