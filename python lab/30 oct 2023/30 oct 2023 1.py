# Dictionary Practice Questions:----

# 1. Write a program to check whether a given key exists in a dictionary or not.
def dictinput():
    n = int(input("Enter no. of key value pair u want in dictionary"))
    dictionary = {}
    for _ in range(n):
        key = input(f"Enter {_+1}th key :")
        value = input(f"Enter {_+1}th value:")
        dictionary[key] = value
    return dictionary


dict1 = dictinput()
print(dict1)
key1 = input("Enter key to check:")
found = False
for key in dict1.keys():
    if key1 == key:
        print("Found")
        found = True


if found == False:
    print("Not Found")


# 2. Write a program in python to map 2 lists into a dictionary.
def listInput():
    mylist = []
    n = int(input("Enter no. of elements u want in the list:"))
    for _ in range(n):
        a = input(f"Enter {_+1} th element:")
        mylist.append(a)
    return mylist


list1 = listInput()
list2 = listInput()
print(dict(zip(list1, list2)))
# 3. Python program to sort dictionary by values (Ascending/ Descending).
sort = sorted(dict1)
print(sort)
# 4. Write a program to get the maximum and minimum value of dictionary.
max = 0
min = float("inf")
for value in dict1.values():
    if max < int(value):
        max = int(value)
    if min > int(value):
        min = int(value)
print(f"max is {max} and min is{min}")


# 5. Write a Python program to concatenate following dictionaries to create a new one.
dictt1 = dictinput()
dictt2 = dictinput()
dictt1.update(dictt2)
print(dictt1)


#  6. Write a Python program to iterate over dictionaries using for loops.
for key, value in dict1.items():
    print(f"{key}:{value}")

# 7. Write a Python program to sum all the items in a dictionary.
print("Enter only numeric expression:")
dictt4 = dictinput()
sum = 0
for key, value in dictt4.items():
    key = int(key)
    value = int(value)
    sum = sum+key+value
print(f"sum is{sum}")

# 8. Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
dict8 = {key: key**2 for key in range(1, 16)}
print(dict8)

# 9. Python program to print all distinct values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
myli = []
for value in dict1.values():
    myli.append(value)

sets = set(myli)
print(sets)
# 10. Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
# dictt10 = {'1': ['a', 'b'], '2': ['c', 'd']}
# thelist = []

# # for value in dictt10.values():
# #     for element in value:
# #         thelist.append(element)
# # print(thelist)

# # for i in thelist:
# i=0
# for value in dictt10.values():
#     value[i]
