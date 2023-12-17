# Q1 Problem Statement
# Tina went to a fruit market to buy some fruits. She filled her fruit basket with different types
# of fruits all together. But the vendor now asked Tina to separate each type of fruit and count
# them, so that he can make the bill. Each type of fruit has a particular number written on it. Tina
# finds it difficult to do so. Help her to count the number of fruits of each type.
# You have given a list A of size N, which stores the number written on each fruit in the basket.
# Your task it to count the number of fruits of each type.
# Input Format:
# The first line contains an integer N denoting the total number of fruits in the basket
# The next N line contains N integers in sorted order representing the fruit number on each type of fruit.
# Output Fomrat:
# For each fruit type, print in a new line, print the number written on the fruit and the count of that fruit
# in the basket separated by space.
# CONSTRAINTS:
# 1<=N<=100
# 1<=A[i]<=100
# Sample Input:
# 7 #N: Number of fruits
# #list of N numbers in sorted order denoting the fruit type
# 1
# 1
# 1
# 2
# 3
# 3
# 4
# Sample Output:
# 1 3 #here 1 is the number written on fruit, and the count of fruit is 3
# 2 1 #here 2 is the number written on fruit, and the count of fruit is 1
# 3 2
# 4 1

n = int(input())

mylist = []
for i in range(n):
    a = int(input())
    mylist.append(a)

dict = {}

for i in mylist:
    count = 0
    for j in mylist:
        if(i == j):
            count += 1
            dict[i] = count

print(dict)
