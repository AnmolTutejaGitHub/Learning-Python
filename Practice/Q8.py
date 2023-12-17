# Q1 Problem Statement
# Input a list from the user that contains car brand names. The task is to find the length
# of each brand name and print it. Also print the concatenated output of brands with the
# maximum length.
# Input Format:
# Enter the number of brands: n (integer value)
# Output Format:
# Concatenated string with maximum number of characters
# Sample input
# 3
# Volvo
# Bentley
# Porsche
# Sample output:
# 5
# 7
# 7
# Bentley Porsche
# Input 1:
# 3
# Polonez
# Audi
# Porsche
# Output:
# 7
# 4
# 7
# Polonez Porsche
# Input 2:
# 3
# Charmant
# Jeep
# Chrysler
# Output:
# 8
# 4
# 8
# Charmant Chrysler
# Input 3:
# 3
# Toyota
# Tesla
# Trofeo
# Output:
# 6
# 5
# 6
# Toyota Trofeo
# Input 4:
# 2
# Tata
# Ferrari
# Output:
# 4
# 7
# Ferrari
# Input 5:
# 2
# Mercedes
# Maverick
# Output:

# 8
# 8
# Mercedes Maverick
# Input 6:
# 3
# Maruti
# Hyundai
# Honda
# Output:
# 6
# 7
# 5
# Hyundai

n = int(input())

mylist = []
for i in range(n):
    s = input()
    mylist.append(s)


lengthList = []
for car in mylist:
    lengthList.append(len(car))
    print(len(car))


# now finding maximum
max = float("-inf")
for _ in lengthList:
    if(_ > max):
        max = _

ans = ''
for car in mylist:
    if len(car) == max:
        if ans != '':
            ans += ' '+car
        if ans == '':
            ans += car


print(ans)
