fptr=open("demofile.txt","r")
#entire file read
#contents=fptr.read();
#print(contents)
#--------------------------------------------------
#read only specified number of charcter
#contents=fptr.read(10);
#print(contents)
#--------------------------------------------------
#read entire line
#contents=fptr.readline();
#contents=fptr.readline();
#print(contents)
#--------------------------------------------------
contents=fptr.readline(2);
print(contents)
contents=fptr.readline(5);
print(contents)

fptr.close()
    
