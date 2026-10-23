#                       Automorphic number

def Automorphic(n):
    origianal = str(n)
    square = str(n * n)
    if square.endswith(origianal):
        print("Automorphic number")
    else:
        print("not Automorphic")
        
Automorphic(6)
Automorphic(7)
