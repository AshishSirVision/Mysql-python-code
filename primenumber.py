lower=int(input("enter lower range:"))
upper=int(input("enter upper range:"))
for num in range(lower, upper +1):
    num>1
    for i in range(2,num):
        if(num % i)==0:
            break
    else:
        print(num)
