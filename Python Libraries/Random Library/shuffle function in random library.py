#shuffle function in random library 
from random import shuffle

mylist=[1,2,3,4,5,6,7,8,9,10,11]

shuffle(mylist)
print(mylist)

random_list=shuffle(mylist) #shuffle function doesn't return anything 
print(random_list) #shuffle function is NoneType
print(type(random_list))

      




