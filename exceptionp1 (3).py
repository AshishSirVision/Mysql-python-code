#exception Handling
print("Program start")
a=12;
b=0;
try:
    ans=a/b#when exception occur redirect to except block
    print(ans)#when exception not occur
except ZeroDivisionError as e:
    print(e)
    
print("Program finish")
