#Lambda function

def square(num):
    return num**2

print(square(5))

mynums=[1,2,3,4,5]
n=9
a=lambda n: n**2
print(a)  #NOT common as we dont intended to use lambda again

#using map
print(list(map(lambda num:num**2,mynums)))

names=['Ganesh','Ram','Krishna']

print(list(map(lambda x:x[0],names)))

#using filter function
print(list(filter(lambda num:num%2==0 , mynums)))




