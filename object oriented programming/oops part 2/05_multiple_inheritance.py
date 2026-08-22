#                                multiple inheritance

class A:
    varA = "welcome to class A"

class B:
    varb = "welcome to class B"

class C(A, B):
    varc = "welcome to class C"

c1 = C()

print(c1.varc)
print(c1.varb)
print(c1.varA)