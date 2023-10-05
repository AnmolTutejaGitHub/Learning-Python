# triangular star
# *
# **
# ***
# ****

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end='')
        j = j+1  # condition for loop termination otherwise infinte loop
    print()
    i = i+1
