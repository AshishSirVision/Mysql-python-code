#custom exception
class AgeEligibleError(Exception):
    pass
#custom message--user defined message
age=19
try:
    if(age<18):
        raise AgeEligibleError('you are not eligible to vote')
    else:
        print("you are eligible to vote")
except AgeEligibleError as e:
    print(e)
