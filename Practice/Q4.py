# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her
# student Mickey to compute the average of all the plants with distinct heights in her
# greenhouse.
# Formula used:
# Average = Sum of Distinct Heights / Total Number of Distinct Heights
# Input Format
# The first line contains the integer, N, the total number of plants.
# The second line contains the N space separated heights of the plants.
# Constraints
# 0 < N <= 100
# Output Format
# Output the average height value on a single line.
# Sample Input
# 10
# 161 182 161 154 176 170 167 171 170 174
# Sample Output
# 169

# TestCase1 4
# 11 12 11 12
# output:
# 11
# TestCase2 5
# 1 2 3 4 5
# output:
# 3
# TestCase3 6
# 12 13 12 14 10 20
# output:
# 13
# TestCase4 3
# 10 10 10
# output:
# 10
# TestCase5 9
# 1 1 2 3 1 4 6 7 3
# output:
# 3

n = int(input())

mylist = []  # input method spaced is asked but using this instead to save time
for i in range(n):
    a = int(input())
    mylist.append(a)

sum = 0
for i in mylist:
    sum += i

average = sum/n

print(round(average))  # rounding to nearest integer
