# 1.  Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'Programming'
# Expected Result : 'Prng'
# Sample String : 'Hi'
# Expected Result : 'HiHI'
# Sample String : ' H'
# Expected Result : Empty String

str = input("Enter a string: ")
end = len(str)
if end < 2:
    print(" ")
else:
    print(str[0:2]+str[-2]+str[-1])

# 2.  Get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

# s=input("Enter a string: ")

# mylist= [x for x in s if x not in s else x=="$" ]
# print(mylist)


# 3.  WAP to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

s1 = input("Enter string1 :")
s2 = input("Enter string2 :")

s12 = s1[0:2]
s22 = s2[0:2]
print(s22+s1[2::]+" "+s12+s2[2::])


# 4. WAP to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

st = input("Enter a string: ")

if len(st) < 3:
    print(st)
elif "ing" in st:
    print(st+"ly")
else:
    print(st+"ing")

# 5.  Write a program to find out the largest and smallest word in the string "This is a Python Programming Language".

# why the fuck que 5 not working

stri = input("Enter a string: ")
mylist = stri.split()
print(mylist)

max = 0
maxword = ""
min = float("inf")
minword = ""

for _ in mylist:
    if len(_) > max:
        max = len(_)
        maxword = _
    if len(_) < min:
        min = len(_)
        minword = _

print(maxword, minword)

# 6.  WAP check if the two strings entered by user are anagrams or not. Two words are said to be anagrams if the letters of one word can be rearranged to form the other word. For example, jaxa and ajax are anagrams of each other.
# a1=input("Enter first word:")
# a2=input("Enter second word:")

# for i in range(0,len(a1))
