#                              move all negative numbers to the left

nums = [3, -1, 4, -2, -5, 8, 7]

left = []

for i in nums:
    if i < 0:
        left.append(i)
for num in nums:
    if(num > 0):
        left.append(num)

print(left)