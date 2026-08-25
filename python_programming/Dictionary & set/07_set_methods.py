#                                     methods of set

nums = set()

print(type(nums))
nums.add(4)  # adds an element
nums.add(2)
nums.add(4)

print(nums)

nums.remove(4)  # removes the elem an
print(nums)

nums.clear()    # empties the set
print(len(nums))

##

hello = {"music", "langunage", "light", "plants"}

print(hello.pop()) #reoves a random value

nums1 = {2, 4, 5, 8, 9}
nums2 = {2, 5, 3, 7, 9}

print(nums1.union(nums2)) # combines both set values & returns new


var1 = {2, 7, 5, 8, 9}
var2 = {5, 9, 3, 4, 7}

print(var1.intersection(var2)) # combines common values & returns new
