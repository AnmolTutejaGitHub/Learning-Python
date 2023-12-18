# Rohan and Ajay are playing a game. The game says, they have been given a list of numbers and they
# have to find out a pair in the list having maximum sum. Ajay is confused and is not able to find the
# required pair, help him to find the solution.
# You have given a list A containing N elements. Your task is to find the pair of numbers in the list
# having maximum sum.
# Write a python program which takes the size N and the list A as input and print the maximum sum
# pair separated by space as the output.
# INPUT FORMAT:
# The first line contains an integer N denoting the total number of elements in the list
# The next N line contains N integers representing the elements in of the list
# OUTPUT FORMAT:
# Print in a single line, the pair of elements from the list having the maximum sum
# CONSTRAINTS:
# 1<N<=100
# 1<=A[i]<=100
# EXAMPLE:
# INPUT:
# 5 #N: number of elements
# 6 #N elements
# 1
# 3
# 2
# 5
# OUTPUT:
# 6 5

n = int(input())

mylist = []
for i in range(n):
    a = int(input())
    mylist.append(a)

max = float("-inf")
secondMax = float("-inf")
for i in mylist:
    if(i > max):
        secondmax=max
        max = i
    elif i > secondMax:
        secondMax = i

print(max, secondMax)
