#                                   remove duplicate value in list without order changing

nums = [1, 2, 2, 3, 1, 4]


def remove_dupli(nums):
    not_duplicate = []
    for num in nums:
        if num not in not_duplicate:
            not_duplicate.append(num)
    return not_duplicate

result = remove_dupli(nums)
print("Remove duplicate : ", result)