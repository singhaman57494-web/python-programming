#                         check if 2 sete are disjoint

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

def disjoint():
    for num in set1:
        if num in set2:
            return False
        
    return True

print(disjoint())
