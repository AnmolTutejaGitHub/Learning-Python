#Map Function
def square(num):
    return num**2

my_nums=[1,2,3,4,5]

print(map(square,my_nums))  #map is user to apply function to all of the list
#map square function to whole list

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

#otherwise I have to do 

for items in my_nums:
   print(square(items))