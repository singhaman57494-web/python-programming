#                    longest consecutive sequence

nums = [100, 4, 200, 1, 3, 2]

longest = 0

for i in nums:
    if i - 1 not in nums:
        current = i
        current_length = 1
        while current + 1 in nums:
            current += 1
            current_length += 1
        if current_length > longest:
            longest = current_length

print("The longest is : ", longest)

        



