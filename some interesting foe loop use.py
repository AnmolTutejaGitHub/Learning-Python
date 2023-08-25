#touple unpacking 
mylist=[(1,2),(3,4),(5,6),(7,8)]

for item in mylist:
     print(item)    

for (a,b) in mylist:
    print(a)
    print(b)

for a,b in mylist:
     print(b)

thislist=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in thislist:
     print(b)

 #another useful way to use for loop
for _ in "hello world":
     print('cool!') #print as many times as there is length of hello world
    

#for(int i=0;i<10;i++)
for i in range (10, -1):  #-1 not included
     print (i)

for i in range(10,0,-1): #-1 is update condition here 
     print(i)

# for i in range(0,10,i*i): #i*i is update condition here
#     print(i)

#3rd argument of range function is step value
for i in range(0,10,2):
     print(i)

#if u want to print numbers that corresponds to the index i*i then:
for i in range(0,100):
     i=i*i
     print(i)
  
#how to iterate through a dictionary
d={'k1':1,'k2':2,'k3':3}

for i in d:
     print(i) #will only iterate through keys of dictionaries

for i in d.items():
     print(i)

for (key,value) in d.values():   #using touple unpacking
     print(value)
