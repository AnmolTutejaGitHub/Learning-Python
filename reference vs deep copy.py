#############

# reference copy or shallow copy
l1 = [1, 8, 76, 0, 9, 567, 3]
l2 = l1

l2[1] = 0
print(l1)  # [1, 0, 76, 0, 9, 567, 3]


# deep copy
l3 = l1.copy()
l3[0] = 0
print(l1)  # [1, 0, 76, 0, 9, 567, 3]
