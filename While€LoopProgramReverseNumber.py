#program based on while loop
#sum ofn digits n=4356--->4+3+5+6=18
num=43562
rev=0
rem=num%10 #2
rev=(rev*10)+rem#0*10 + 2=2
num=num//10#4356
print(rem,rev,num)

rem=num%10 #6
rev=(rev*10)+rem#2*10 + 6=20+6=26
num=num//10#435
print(rem,rev,num)

rem=num%10 #5
rev=(rev*10)+rem#26*10 + 5=260+5=265
num=num//10#43
print(rem,rev,num)

rem=num%10 #3
rev=(rev*10)+rem#265*10 + 3=2650+3=2653
num=num//10#4
print(rem,rev,num)

rem=num%10 #4
rev=(rev*10)+rem#2653*10 + 4=26530+4=26534
num=num//10#0
print(rem,rev,num)

################################
print("----------while loop-------------")
num=1234567
rev=0
while(num!=0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
    print(rem,rev,num)
