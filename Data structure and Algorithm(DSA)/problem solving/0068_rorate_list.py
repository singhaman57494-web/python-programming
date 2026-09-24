#                                Rotate list Right by 1

nums = [1, 2, 3, 4, 5]


temp = nums[-1]

for i in range(len(nums) - 1, 0, -1):
    nums[i] = nums[i - 1]

nums[0] = temp
    

print(nums)