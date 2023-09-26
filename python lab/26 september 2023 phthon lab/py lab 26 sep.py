# 1. Write a program that accepts a list from user and print the alternate element of list.
n = int(input("Enter no of elements u want in list :"))

mylist = []

print("Enter elements ")
for i in range(n):
    a = int(input())
    mylist.append(a)

altlist = []
for i in range(len(mylist)):
    if i % 2 == 0:
        altlist.append(mylist[i])

print(altlist)


# 2. Write a program that accepts a list from user. Your program should reverse the content of list and display it.
# Do not use reverse() method.
print(mylist[::-1])

# 3. Find and display the largest number of a list without using built-in function max().
# Your program should ask the user to input values in list from keyboard.
maxi = float("-inf")  # max=mylist[o]

for i in mylist:
    if i > maxi:
        maxi = i

print(maxi)


# Question 4: You are given a list of words. Write a Python program to find and group all the anagrams from the list.
#  Anagrams are words or phrases formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
# For example, "listen" and "silent" are anagrams of each other.

# Your program should accomplish the following:

# Read a list of words from the user, where each word is separated by a space.
# Group words that are anagrams of each other into separate lists.
# Print each group of anagrams together.
