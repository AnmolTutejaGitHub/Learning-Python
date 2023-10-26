# doc string in python , PEP8

# python doc strings are the string literals that appear rigth after the definition of a function ,method,class or module
def square(n):
    '''Take in a number n and returns the square of n '''  # this is doc string and it's different from comment , python does not ignorte doc string unlike comments
    print(n**2)


square(5)  # 25

# will print doc string #Take in a number n and returns the square of n
print(square.__doc__)

# below code ke liye doc string none hogi
# as rigth after function definiton


def square2(n):
    print(n)
    '''Take in a number n and returns the square of n '''  # this is doc string and it's different from comment , python does not ignorte doc string unlike comments
    print(n**2)


square2(5)  # 25

print(square2.__doc__)  # none

# doc string must be placed rigth below/right above function name/defintion


# PEP8
#import this
# zenth of python
