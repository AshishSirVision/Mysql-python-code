age=12
try:
    if(age<18):
        raise ValueError('you are not eligible to vote')
    else:
        print("you are eligible to vote")
except ValueError as e:
    print(e)
