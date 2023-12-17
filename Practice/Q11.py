# #Problem Statement:
# You are in-charge of the cake for your niece's birthday and have decided the cake will have
# one candle for each year of her total age. When she blows out the candles, she’ll only be able
# to blow out the tallest ones.
# For example, if your niece is turning 5 years old, and the cake will have candles of height
# 4,2,4,3,4 she will be able to blow out 3 candles successfully, since the tallest candle is of height
# 4 and there are 3 such candles.
# Given the height of each individual candle, find and print the number of candles she can
# successfully blow out.
# Input Format
# The first line contains a single integer, n ,denoting the number of candles on the cake.
# The second line contains n line-separated integers, where each integer describes the height of candle i.
# Output Format
# Print the number of candles the can be blown out on a new line.
# For Example:
# Sample Input
# 5
# 4
# 2
# 4
# 3
# 4
# Sample Output
# 3
# Explanation:
# We have one candle of height 2 , one candle of height 3, and rest of the three candles of height
# 4 . Your niece only blows out the tallest candles, meaning the candles where height=4 . Because
# there are 3 such candles, we print 3 on a new line as output.

n = int(input())

s = input()
numlist = s.split(' ')

max = float('-inf')
for _ in numlist:
    if int(_) > max:
        max = int(_)

count = 0
for i in numlist:
    if int(i) == max:
        count += 1

print(count)
