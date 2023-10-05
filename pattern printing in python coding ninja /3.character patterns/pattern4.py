# E
# DE
# CDE
# BCDE
# ABCDE

# ref : 4th que of this triangular pattern que10
n = int(input())

i = 1
while i <= n:
    j = i
    while j <= i:
        startChar = chr(n+i-1+j-1)
        print(startChar, end='')
        j = j-1
        # startChar = chr(ord(startChar)+i)

    print()

    i = i+1
