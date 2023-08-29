#LESSER OF EVENS: write a function that returns lesser of two given numbers if both numbers are even but returns
#the greater if one or both numbers are odd

def myfunc(a,b):
    if a%2==0 and b%2==0:
        small=a
        if b<a:
            small=b
        return small
    else:
        large=a
        if b>a:
            large=b
        return large
    

print(myfunc(5,4))
print(myfunc(2,4))
