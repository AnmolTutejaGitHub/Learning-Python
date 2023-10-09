# Write a program that accepts a list from user.
# Your program should reverse the content of list and display it. Do not use reverse () method.

n = int(input("enter number of elements of the list: "))

mylist = []
for _ in range(1, n+1):
    a = input(f"Enter {_}th element of the list  : ")
    mylist.append(a)

reversedList = []

for item in mylist:
    reversedList.insert(0, item)  # insert item to the beginning of the list

print(f"reversed list is {reversedList}")

# Find and display the largest number of a list without using built-in function
# max (). Your program should ask the user to input values in list from keyboard.
b = int(input("enter number of elements of the list: "))
thelist = []
for i in range(1, b+1):
    c = int(input(f"Enter {i}th element of the list  : "))
    thelist.append(c)

max = float("-inf")  # max=mylist[o]

for i in thelist:
    if i > max:
        max = i

print(f"maximum element is {max}")
