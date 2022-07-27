m1=[[0,0,0],[0,0,0],[0,0,0]]
m2=[[0,0,0],[0,0,0],[0,0,0]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
def fun1logic(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end=" ")
        print()

def userinput():
    m=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j]=int(input("at pos %d,%d :"%(i,j)))
        print()
    return m
def calfun(m1,m2,op):
    m3=[[0,0,0],[0,0,0],[0,0,0]]
    if(op=='+'):
        for i in range(len(m2)):
            for j in range(len(m2[i])):
                m3[i][j]=m1[i][j]+m2[i][j];
        print()
    elif(op=='-'):
        for i in range(len(m2)):
            for j in range(len(m2[i])):
                m3[i][j]=m1[i][j]-m2[i][j];
        print()
        
    return m3
print("Enter The elements for Matrix 1: ")
m1=userinput();
print("Enter The elements for Matrix 2: ")
m2=userinput();
    
m3=calfun(m1,m2,'-')
    
print("____________")
print("the matrix m1")
fun1logic(m1)

print("____________")
print("the matrix m2")
fun1logic(m2)

print("___________")
print("the matrix m3=m1-m2")
fun1logic(m3)
        
