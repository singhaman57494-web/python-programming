nums = [45, 12, 78, 28, 56, 69, 34]

target = 56

for i in range(len(nums)):
    if nums[i] == target:
        target = nums[i]

print(target)