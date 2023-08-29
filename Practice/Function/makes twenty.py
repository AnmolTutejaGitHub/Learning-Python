#MAKES TWENTY:given two integers , return True if the sum of the integers is 20 or if one of the integer is 20.If not return False

def myfunc(a,b):
    if a==20 or b==20 or a+b==20 :
        return True
    else:
        return False
    

print(myfunc(20,8))
print(myfunc(45,98))
print(myfunc(10,10))
print(myfunc(0,20))