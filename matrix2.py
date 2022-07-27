m1=[[0,0,0],[0,0,0],[0,0,0]]
m2=[[0,0,0],[0,0,0],[0,0,0]]
m3=[[0,0,0],[0,0,0],[0,0,0]]

print("Enter The elements for Matrix 1: ")
for i in range(len(m1)):
    for j in range(len(m1[i])):
        m1[i][j]=int(input("at pos %d,%d :"%(i,j)))
    print()
print("Enter The elements for Matrix 2: ")
for i in range(len(m2)):
    for j in range(len(m2[i])):
        m2[i][j]=int(input("at pos %d,%d :"%(i,j)))
        m3[i][j]=m1[i][j]+m2[i][j];
    print()

print("____________")
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

print("___________")
print("the matrix m3=m1+m2")
for i in range(len(m3)):
    for j in range(len(m3[i])):
        print(m3[i][j],end=" ")
    print()
        
