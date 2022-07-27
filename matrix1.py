m1=([0,0,0],[0,0,0],[0,0,0])
m2=([0,0,0],[0,0,0],[0,0,0])
m3=([0,0,0],[0,0,0],[0,0,0])

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
print(m1)
print(m2)
print(m3)
