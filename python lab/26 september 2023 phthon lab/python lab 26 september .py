# Write a Python program that performs the following operations on the list:

# Find and print the sum of all the numbers in the list.
mylist = [1, 2, 3, 7, 9, 9, -1, 0, -7]
sum = 0
for i in mylist:
    sum = sum+i
print(sum)
# Find and print the maximum and minimum values in the list.
max = float("-inf")  # max=mylist[o]
min = float('inf')

for i in mylist:
    if i > max:
        max = i

    if i < min:
        min = i

print(max, min)

# Find and print the average of the numbers in the list.
avg = 0
for i in mylist:
    avg = avg+i
avg = avg/len(mylist)
print(avg)

# Create a new list that contains only the even numbers from the original list.
newlist = []
for i in mylist:
    if i % 2 == 0:
        newlist.append(i)
print(newlist)

# Create a new list that contains the squares of all the numbers in the original list.
sqlist = []
for i in mylist:
    sqlist.append(i**2)
print(sqlist)

# Sort the original list in ascending order and print it.
# sorting
# cpylist = mylist
# sortedlist = []

# for i in cpylist:
#     sortedlist.append(min)
#     cpylist.remove(min)
#     min = float("inf")
#     for j in cpylist:
#         if j < min:
#             min = j

# print(sortedlist)
