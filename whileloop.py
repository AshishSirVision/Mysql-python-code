i=10
while(-1>=0):
    print(i,end=', ')
    i=i-1

print("\n------- display 1 to 10-------------")
for i in range(10,1-1,-1):
    print(i,end=', ')
   
print("\n-------display 1 to 10 -------------")
for i in range(10,0,-2):
    print(i,end=', ')

print("\n--------------------")
for i in range(10,0,-2):
    print(i,end=', ')

print("\n--------------------")
for i in range(0,11,2):
    print(i,end=', ')

print("\n---------while loop 1 to 150-----------")
i=0
while(i<15):
    print(i,end=', ')
    i=i+1


print("\n--------------------")
for i in range(0,151,30):
    if(i==0):
        print("1",end=", ")
        continue
    print(i,end=', ')
       
print("\n--------------------") 
for i in range(0,151,30):
    if(i==90):
        print("1",end=", ")
        break;
    print(i,end=', ')
       
    
