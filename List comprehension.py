#List comprehension

#long method
mystring='hello'
mylist=[]
for item in mystring:
    mylist.append(item)

print(mylist)

#list comprehension
mystring='hello'
mylist=[item for item in mystring]
print(mylist)

mylist=[x for x in range(0,10)]
print(mylist)

mylist=[x for x in 'word']
print(mylist)

#can also perform operations
mylist=[num**2 for num in range(0,11)]
print(mylist)

mylist=[]
for num in range(0,11):
    mylist.append(num**2)
print(mylist)

mylist=[x for x in range(0,11) if x%2==0]

mylist=[x**2 for x in range(0,11) if x%2==0]


celcius=[0,10,20,34.5]
fahrenheit=[((9/5)* temp +32) for temp in celcius]
print(fahrenheit)
#OR

fahrenheit=[]
for temp in celcius:
    fahrenheit.append((9/5)*temp+32)
print(fahrenheit)

#using if-else statement in list comprehension
result=[x if x%2==0 else 'ODD' for x in range(0,11) ]

#nested loop
mylist=[]
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)

#using list comprehension
mylist=[x*y for x  in [2,4,6] for y in [100,200,300]]
print(mylist)
