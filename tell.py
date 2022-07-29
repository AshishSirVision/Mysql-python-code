fptr=open("demofile.txt","r")
contents=fptr.read(10);
print(contents)
print(" the current position of file pointer : ",fptr.tell())
fptr.seek(fptr.tell()+5)
contents=fptr.read(50);
print(contents)
fptr.close()
    
