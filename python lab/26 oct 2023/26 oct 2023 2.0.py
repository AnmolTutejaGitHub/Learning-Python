# 1.      Return a new set of identical items from two sets.
def inputSet():
    n = int(input("Enter no of elements u want to enter in the set:"))
    sets = set()
    for _ in range(n):
        n2 = input(f"Enter {_+1}th element :")
        sets.add(n2)
    return sets


set1 = inputSet()
set2 = inputSet()

setoutput = set1.intersection(set2)
print(setoutput)


# 2.      Return a set of elements present in Set A or B, but not both
set3 = set((set1-set2).union(set2-set1))
print(set3)
# 3.      Check if two sets have any elements in common. If yes, display the common elements.
print(set1.intersection(set2))
# 4.      Remove items from set1 that are not common to both set1 and set2.
# toRemoveList = list(set1-((set1-set2).union(set2-set1)))
# # print(toRemoveList)

# for _ in toRemoveList:
#     set1.remove(_)
# print(set1)
# 5.      Python Program to Count Number of Vowels in a Given String Using Sets.
# string = input("Enter the string:").lower()
# stringSet = set(string)
# stringlist = list(string)
# vowellist = ["a", "e", "i", "o", "u"]

# count = 0
# for _ in stringlist:
#     if(_ == "a" or "e" or "i" or "o" or "u"):
#         count = count+1

# print(count)


str = input()
count = 0
setS = set("aeiouAEIOU")
for char in str:
    if char in setS:
        count += 1
print(count)
