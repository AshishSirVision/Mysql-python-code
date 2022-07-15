a=[2,3,4,5,6,5,6,6,86,8,0,405,4,4,3,3,9]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#---display list elements using for loop
for i in range(0,len(a)):
    print("Elemets at %d index :%d"%(i,a[i]))
#string
a="Hello World"
for i in range(0,len(a)):
    print("Elemets at %d index :%s"%(i,a[i]))

##########stop printing when get value empty
s="Hello-World"
for k in range(0,len(s)):
    if(s[k]=="-"):
        break
    print("Elemets at %d index :%s"%(k,s[k]))
##########skip printing when get value o
s=" tom is tom tom is tom"
for k in range(0,len(s)):
    if(s[k]=="o" or s[k]==" "):
        continue
    print("Elemets at %d index :%s"%(k,s[k]))
