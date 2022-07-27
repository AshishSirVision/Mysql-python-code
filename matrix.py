a=[[1,2,3],[4,6,8],[5,7,9]]
b=[[1,4,7],[2,5,8],[3,6,9]]
c=len(a)
print("the matrix A=")

for i in range(c):
    for j in range(c):
        print(a[i][j],end=" ")
    print()

print("the matrix B=")
for i in range(c):
    for j in range (c):
        print(b[i][j],end=" ")
    print(" ")

print("the matrix A+B=")
for i in range(c):
    for j in range (c):
        print(a[i][j]+b[i][j],end=" ")
    print()


