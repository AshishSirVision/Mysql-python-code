#exception Handling
print("Program start")
try:
    ans=int("1u")
    print(ans)#when exception not occur
except ValueError as e:
    print(e)
    
print("Program finish")
