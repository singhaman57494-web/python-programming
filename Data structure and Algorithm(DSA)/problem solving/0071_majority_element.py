#                            find the majority Element

nums = [2, 2, 1, 1, 1, 2, 2]
count = {}
majority = 0

for num in nums:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

for num in count:
    if count[num] > len(nums) / 2:
        majority = num

print("Majority number is : ", majority)