# 1.      Write a Program in Python to Find the Differences Between Two Lists Using Sets.

mylist1 = [1, 2, 45, 6, 7, 8, 3, 4]
mylist2 = [1, 5, 6, 7, 8, 45]
set1 = set(mylist1)
set2 = set(mylist2)
result = (set1-set2).union(set2-set1)
print(result)


# // 2.      Python Program to Check if a Given String Is Heterogram or Not

# // A string is a heterogram if it has no alphabet that occurs more than once. For example, “ChitkaraUniversity” is not a heterogram.
#  However, “abc def ghi jkl” is a heterogram. You can follow the below steps to check if a given string is a heterogram or not.

# // •           Separate all the alphabets from other any other characters (using list comprehension)

# // •           Convert list of alphabets into set because set has unique elements (using set())

# // •           Check if the length of the set is equal to number of alphabets

# // •           If yes, then string is heterogram otherwise its not

def isHetrogram(string):
    mylist = list(string)
    # print(mylist)
    sets = set(mylist)
    # print(sets)
    if len(mylist) == len(sets):
        return f"{string} IS HETEROGRAM"
    else:
        return f"{string} IS NOT A HETEROGRAM"


print(isHetrogram("abc"))
print(isHetrogram("Chitkara university"))


# 1.      Return a new set of identical items from two sets.
# 2.      Return a set of elements present in Set A or B, but not both
# 3.      Check if two sets have any elements in common. If yes, display the common elements.
# 4.      Remove items from set1 that are not common to both set1 and set2.
# 5.      Python Program to Count Number of Vowels in a Given String Using Sets.
