# 2 dimentional array question

#  Samita is assigned a task by her class teacher to convert a list into 2-d list. Help Samita to
# complete her task. The task detail is given below:
# Given a list, the task is to split the list at every Nth element and create a 2-d list.
# Sample Input format:
# n-→nth element for splitting
# list-→ single line input list of any length
# Output format:
# 2d list
# Sample Input
# 4
# 4 5 6 7 8 9 1 2 3 4 5 6 6
# Sample Output:
# [['4', '8', '3', '6'], ['5', '9', '4'], ['6', '1', '5'], ['7', '2', '6']]


# Testcases
# Test Case1 Input
# 3
# 1 2 3 45 6 2 3 7
# Output
# [['1', '45', '3'], ['2', '6', '7']
# , ['3', '2']]
# Test Case2 Input
# 2
# 1 2 3 4 5
# Output
# [[‘1’,‘3’,‘5’],[‘2’, ‘4’]]
# Test Case3 Input
# 1
# 1 2 3 4 5
# Output
# [['1', '2', '3', '4', '5']]
# Test Case 4 Input
# 4
# 1 2 3 4 5
# Output:
# [['1', '5'], ['2'], ['3'], ['4']]
# Test Case 5 Input
# 5
# 1 2 3 4 5
# Output
# [['1'], ['2'], ['3'], ['4'], ['5']]

n = int(input())
s = input()
slist = s.split(' ')

print(slist)

output = [slist[i::n] for i in range(n)]
print(output)
