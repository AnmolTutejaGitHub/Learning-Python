#write a python function to multiply all the numbers in a list
#sample list = [1,2,3,-4]
#expected output = -24

def multiply(numbers):
    total=1 #as 1 times n is n
    for num in numbers:
        total=total*num
    return total 

print(multiply([1,2,3,-4]))