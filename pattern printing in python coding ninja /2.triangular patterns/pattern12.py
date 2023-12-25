#     *
#    ***
#   *****
#  *******
# *********

n = int(input())

# i = 1
# while i <= n:
#     k = 1
#     while k <= n - i:
#         print(" ", end="")
#         k += 1

#     j = 1
#     while j <= 2 * i - 1:
#         print("*", end="")
#         j += 1

#     print()

#     i += 1

i = 1
while i <= n:
    j = 1
    while j <= 2*n - 1:
        if j >= n-(i-1) and j <= n+(i-1):
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
