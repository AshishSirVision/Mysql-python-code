a=12;
b=0
#custom message--user defined message
try:
    if(b==0):
        raise ZeroDivisionError('Divide by zero not allowed in maths ')
    else:
        print("you are eligible to vote")
except ZeroDivisionError as e:
    print(e)
