m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[2,1,3],[6,5,4],[9,8,7]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
print("the matrix m1")
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(m1[i][j],end=" ")
    print()

print("____________")
print("the matrix m2")
for i in range(len(m2)):
    for j in range(len(m2[i])):
        print(m2[i][j],end=" ")
    print()

for i in range(len(m2)):
    for j in range(len(m2[i])):
        m3[i][j]=m1[i][j]+m2[i][j];


print("___________")
print("the matrix m3=m1+m2")
for i in range(len(m3)):
    for j in range(len(m3[i])):
        print(m3[i][j],end=" ")
    print()
        
