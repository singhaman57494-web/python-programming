r = int(input("enter the row : "))
c = int(input("enter the column"))

a = []
b = []

print("enter the matrix: ")

for i in range(r):
    row = list(map(int, input().split))
    a.append(row)

print("enter second matrix : ")

for i in range (r):
    row = list(map(int, input().split()))
    b.append

result = []

for i in range(r):
    row = []

    for j in range(c):
        row.append(a[i][j] + b [i][j])

        result.append(row)

print("amtrix addition : ")

for row in result:
    print(row)