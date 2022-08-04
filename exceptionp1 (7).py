#exception Handling
print("Program start")
name=None
list1=[2,3]
try:
    #ans=int("1u")
    l=len(name)
    #elements=list1[5]
    print("try block")
except Exception as e:
    print(e)
finally:
    print("this block always executed when Exception occur or not")

    
print("Program finish")
