#exception Handling
print("Program start")
try:
    #ans=int("1u")
    print("try block")
except Exception as e:
    print(e)
else:
    print("else block executed when except block not executed")

    
print("Program finish")
