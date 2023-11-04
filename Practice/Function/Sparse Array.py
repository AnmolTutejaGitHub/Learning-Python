# Sparse Array
# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
# Example:
# stringList=["ab","ab","abc"]
# queries=["ab","abc","bc"]
# There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, results=[2,1,0]
# Function Description
# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in stringList.
# matchingStrings has the following parameters:
#    string stringList[n] - an array of strings to search
#    string queries[q] - an array of query strings
# Returns
#  int[q]: an array of results for each query

# Input Format

# The first line contains and integer n , the size of stringList[]
# Each of the next n lines contains a string stringList[i].
# The next line contains q, the size of queries[].
# Each of the next q  lines contains a string queries[i].


# my code failing certain test cases

def sArray(s, q):
    arr = []  # to store count
    arr = [0]*len(q)
    for i in q:
        for j in s:
            if i == j:
                a = q.index(i)
                arr[a] = arr[a]+1
    return arr


n = int(input())
s = []
for _ in range(n):
    a = input()
    s.append(a)

n2 = int(input())
q = []
for _ in range(n2):
    b = input()
    q.append(b)

arr = sArray(s, q)

for item in arr:
    print(item)
