# Problem Statement
# Write a program to do basic string compression. For a character which is
# consecutively repeated more than once, replace consecutive duplicate occurrences
# with the count of repetitions
# Example:
# If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".
# The string is compressed only when the repeated character count is more than 1.
# Note:
# You are not required to print anything. It has already been taken care of. Just
# implement the given function.
# Input Format:
# The first and only line of input contains a string without any leading and trailing
# spaces.

# Output Fomrat:
# The output contains the string after compression printed in single line.
# Constraints :
# 0 <= N <= 10^6
# Where 'N' is the length of the input string.
# Time Limit: 1 sec
# Input 1:
# aaabbccdsa
# Output 1:
# a3b2c2dsa
# Explanation for Sample Output 1:
# In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is repeated 2
# times and 'd', 's' and 'a' and occuring 1 time hence no compression for last 3
# characters.

# TestCase1 Raaakkkkeeeeeeeesssssssssh   Ra3k4e8s9h
# TestCase2 aaabbcddeeeee a3b2cd2e5
# TestCase3 reeeenuuu re4nu3
# TestCase4 Chhhitkaaaraa Ch3itka3ra2
# TestCase5 Heeelllo He3l3o

s = input()

slist = list(s)
final = ''
ans = {}
for i in slist:
    count = 0
    for j in slist:
        if i == j:
            count += 1
            ans[i] = count

print(ans)


for key, value in ans.items():
    if(ans[key] == 1):
        final += key
    elif(ans[key] > 1):
        final += key+str(value)

print(final)
