fobj=open("demofile1.txt","w")
#fobj2=open("inputfile.txt","r")
with open("inputfile.txt","r") as fobj2:
    H=fobj2.read()
    print(H)
#fobj2.close()
for n in range(1,int(H)):
    flag=True #assume any number is prime
    if(n>1):
        for i in range(2,(n//2)+1) :
            if(n%i==0):
                flag=False#this is not prime
                break;
    if(n==0 or n==1):
        fobj.write("neither prime nor composite\n")
        
    elif(flag==True):
        fobj.write(str(n)+" is prime number\n")
    elif(flag==False):
        fobj.write(str(n)+" is not prime number\n")
fobj.close()
    
