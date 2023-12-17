# Task: Ramesh and Rajkumar have M and N sets of Indian currency notes respectively. They
# have decided to donate all those currency notes that are not common to M and N to the social
# welfare society. After receiving them, the society arranged these currency notes in sorted
# order and also display the total amount they received
# Input Format
# The first line contains N space-separated integers.
# The second line contains M space-separated integers.
# Output Format
# The non-common elements are printed in an ascending order separated by one space and also
# print the amount of all currency notes as last elements in the same line as received by the
# social welfare society
# Sample Input
# 1 2 5 10 # set of M currency notes
# 5 10 100 200 # set of N unique currency notes
# Sample Output
# 1 2 100 200 303 # set of noncommon currency notes and the last element (303) is
# the #sum of all (1+2+100+200=303) received by social welfare
# Sample Test Cases
# Case1 Input  Output
# 1 1 2
# 5 10
# Output
# 1 2 5 10 18

# 2 2 5 10 100
# 2 100 200 500
# Output
# 5 10 200 500 715

# 3 5 10 100 1000
# 1 2 500 2000
# Output
# 1 2 5 10 100 500 1000 2000 3618

# 4 1 2 5 10
# 1 2 5 10
# Output
# 0

# 5 1 2 5 10
# 2 5 10 100
# Output
# 1 100 101

m = input()
n = input()

mlist = m.split(" ")
nlist = n.split(" ")

mset = set(mlist)
nset = set(nlist)

diff = mset.symmetric_difference(nset)

difflist = [int(i) for i in list(diff)]
# print(difflist)


sorteddiff = sorted(difflist)


sum = 0
for i in difflist:
    sum += int(i)

print(sorteddiff)
print(sum)
