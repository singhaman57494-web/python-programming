#                          find missing number

nums = [1, 2, 3, 5, 6]
total = 0
nums_sum = 0

for i in range(1, 7):
    total += i 

for i in nums:
    nums_sum += i

missing = total - nums_sum
print("Missing number is : ", missing)