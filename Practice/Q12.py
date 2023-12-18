# Task: Rakesh and Rajkumar have different types of fruits in some quantities. They have been asked to donate all those fruits that are not in common quantities to the orphanage.  The officials of orphanage arranged all these such categories of fruits in the sorted order and also displayed the count of total amount of fruits received from them.    
# Input Format:The first line contains all categories of fruits (in quantities) possessed by Rakesh. The second line contains all categories of fruits (in quantities) possessed by Rajkumar
# Output Format:The uncommon fruits are required to be printed in an ascending order separated by one space and also print the amount of all fruits received by them as last elements in the same line.   Sample Input 1 5 10 2               # set of 4 categories of fruits in quantities of 1, 5, 10 and 2 respectively 10 5 8 200 100   # set of 5 categories of fruits in quantities of 10, 5, 8, 200, 100 respectively   Sample Output   1 2 8 100 200 311
#  # sorted order of uncommon fruits (in quantities) and the last element, (311) is the sum of all (1+2+8+100+200=311) quantities of uncommon categories of fruits

def inputConvertor(n):
    numlist = n.split(' ')
    return numlist


n = input()
m = input()

nlist = inputConvertor(n)
mlist = inputConvertor(m)

nonCommon = set(nlist).symmetric_difference(set(mlist))

nonCommonint = [int(i) for i in nonCommon]

sortedlist = sorted(nonCommonint)

print(sortedlist, sum(sortedlist))
