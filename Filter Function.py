#Filter Function

def check_even(num):
    return num%2==0

mylist=[1,2,3,4,5,6]
print(filter(check_even,mylist))
print(list(filter(check_even,mylist)))

for n in filter(check_even,mylist):
    print(n)
