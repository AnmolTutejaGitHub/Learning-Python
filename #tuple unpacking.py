# tuple unpacking
# touple unpacking
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]

for item in mylist:
    print(item)
 #(1, 2)
 # (3, 4)
 # (5, 6)
 # (7, 8)

for (a, b) in mylist:
    print(a)
    print(b)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

for a, b in mylist:
    print(b)

# 2
# 4
# 6
# 8

thislist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in thislist:
    print(b)
# 2
# 5
# 8
