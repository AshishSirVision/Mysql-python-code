#DATATYPE PROGRAM
a=56
print("Data type of variable a is : "+str(type(a))+" and value is"+str(a))
print("Data type of variable a is : ",type(a)," and value is",a)
print("Data type of variable a is : %s and value is %d"%(type(a),a))

a=56
#format specifiers
print("%s, %s , %f , %i "%("5",True,7.67,8))

for i in range(0,200):
    print("%o"%i)
