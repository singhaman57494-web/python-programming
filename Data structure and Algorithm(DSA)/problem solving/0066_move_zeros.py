#                                      move zeros to end

nums = [0, 1, 0, 3, 12]

move = []

for i in nums:
    if i > 0:
        move.append(i)


for i in nums:
    if i == 0:
        move.append(i)

print(move)
