n = int(input("Enter no of elements u want in list :"))

mylist = []

print("Enter elements ")
for i in range(n):
    a = int(input())
    mylist.append(a)

print(mylist)

mylist.append(9)
mylist.insert(1,45) #1 is index no to insert at
mylist.append([7,97])
mylist.extend([1,2,3])
mylist.remove(45)
mylist.pop()
mylist.pop(2)  #will pop second index

print(mylist[::-1])
 