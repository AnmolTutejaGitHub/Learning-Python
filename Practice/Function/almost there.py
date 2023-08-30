#Almost There : given an integer n, return True if n is within 10 of either 100 or 200
#Example: almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almosst_there(200) --> True

#Note: abs(num) returns the absolute value of a number

def almost_there(n):
    return((abs(100-n)<=10) or (abs(200-n)<=10))

print(almost_there(104))
print(almost_there(150))
print(almost_there(205))
