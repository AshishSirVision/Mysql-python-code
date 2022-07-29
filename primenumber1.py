n=1
flag=True #assume any number is prime
if(n>1):
    for i in range(2,(n//2)+1) :
        if(n%i==0):
            flag=False#this is not prime
            break;
if(n==0 or n==1):
    print("neither prime nor composite")
    
elif(flag==True):
    print(str(n)+" is prime number")
elif(flag==False):
    print(str(n)+" is not prime number")

    
