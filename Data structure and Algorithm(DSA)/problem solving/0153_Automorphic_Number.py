#                      Automorphic Number

def Automorphic(n):
    original = str(n)
    square = str(n * n)

    if square.endswith(original):
        return True
    else:
        return False
    
result = Automorphic(6)

if result:
    print("number is Automorphic")
else:
    print("not Automorphic")