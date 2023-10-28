# 1.      Write a Python program to replace last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
def listTupleInput():
    mytupleList = []
    mylist = []
    n = int(input("Enter No. of items(tuples) u want in list:"))
    for i in range(n):
        a = int(input(f"Enter no. of elemets u  want in {i+1}th tuple:"))
        for I in range(a):
            if(a == 0):
                mytuple = tuple()
                break
            b = input(f"Enter {I+1}th element of {i+1}th tuple:")
            if(b.isdigit()):
                b = int(b)
            mytupleList.append(b)
        mytuple = tuple(mytupleList)
        mytupleList = []
        mylist.append(mytuple)
    return mylist


#mylist = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
mylist = listTupleInput()
# print(mylist)
newlist = []
for i in mylist:
    i = list(i)
    # print(i)
    i[2] = 100
   # print(i[2])
    i = tuple(i)
    newlist.append(i)
    # print(i)
print(newlist)

# 2.      Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
#mylist2 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
mylist2 = listTupleInput()
NewList2 = []
for _ in mylist2:
    if _ != ():
        NewList2.append(_)
print(NewList2)

# 3. Write a Python program to check if a specified element presents in a tuple of tuples.
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White present in said tuple of tuples!
# True
# Check if Olive present in said tuple of tuples!
# False


def tuplestupleInput():
    mytupleList = []
    mylist = []
    n = int(input("Enter No. of items(tuples) u want in list:"))
    for i in range(n):
        a = int(input(f"Enter no. of elemets u  want in {i+1}th tuple:"))
        for I in range(a):
            if(a == 0):
                mytuple = tuple()
                break
            b = input(f"Enter {I+1}th element of {i+1}th tuple:")
            if(b.isdigit()):
                b = int(b)
            mytupleList.append(b)
        mytuple = tuple(mytupleList)
        mytupleList = []
        mylist.append(mytuple)
    mynewtuple = tuple(mylist)
    return mynewtuple


#thetuplestuple = (('Red', 'White', 'Blue'), ('Green', 'Pink','Purple'), ('Orange', 'Yellow', 'Lime'))
thetuplestuple = tuplestupleInput()
n = int(input("Enter the tuple number to be checked :"))
for i in range(len(thetuplestuple[n-1])):
    if thetuplestuple[n-1][i] == "White":
        print("True")
    elif thetuplestuple[n-1][i] == "Olive":
        print("False")


# 4.	Given a Tuple List, perform sort on basis of total digits in tuple.
# Examples:
# Input : test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)]
# Output : [(1, 2), (3, 4, 6, 723), (134, 234, 34)]
# Explanation : 2 < 6 < 8, sorted by increasing total digits.
# Input : test_list = [(1, 2), (134, 234, 34)]
# Output : [(1, 2), (134, 234, 34)]
# Explanation : 2 < 8, sorted by increasing total digits.
