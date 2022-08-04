#exception Handling
print("Program start")
name=None
list1=[2,3]
try:
    #ans=int("1u")
    #l=len(name)
    elements=list1[5]
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except IndexError as e:
    print(e)
    
    

    
print("Program finish")
