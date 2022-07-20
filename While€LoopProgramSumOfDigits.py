#program based on while loop
#sum ofn digits n=4356--->4+3+5+6=18
num=43562
s=0
rem=num%10
s=s+rem
num=num//10
print(rem,s,num)


rem=num%10
s=s+rem
num=num//10
print(rem,s,num)

rem=num%10
s=s+rem
num=num//10
print(rem,s,num)

rem=num%10
s=s+rem
num=num//10
print(rem,s,num)

rem=num%10
s=s+rem
num=num//10
print(rem,s,num)
################################
print("----------while loop-------------")
num=89
s=0
while(num!=0):
    rem=num%10
    s=s+rem
    num=num//10
    print(rem,s,num)
