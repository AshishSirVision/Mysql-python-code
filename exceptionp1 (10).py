#exception Handling
print("Program start")
try:
    c=4/0
    fptr=open("demofile2.txt","r")
except (IOError, ArithmeticError) as e:
    print(e)
finally:
    print("this block always executed when Exception occur or not")

    
print("Program finish")
