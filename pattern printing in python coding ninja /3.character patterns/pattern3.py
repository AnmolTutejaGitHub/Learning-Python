#not working
# update : #I don't know how the fuc' I made this work

# A
# BC
# CDE
# DEFG

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        startChar = chr(ord('A')+i-1+j-1)
        print(startChar, end='')
        j = j+1
        # startChar = chr(ord(startChar)+i)

    print()

    i = i+1
