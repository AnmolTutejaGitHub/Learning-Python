# a) Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string.
# * The number of lowercase letters in the string.
# * The number of digits in the string.
# * The number of whitespace characters in the string.

s = input("Enter the string :")

uppercase = 0
lowercase = 0
digits = 0
whitespace = 0

for i in s:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        lowercase = lowercase + 1
    elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        uppercase = uppercase + 1
    elif i in '0123456789':
        digits = digits + 1
    elif i == ' ':
        whitespace = whitespace+1

print(
    f"uppercase={uppercase},lowercase={lowercase},digits={digits},whitespace={whitespace}")


# Python Program to Find Common Characters in Two Strings.
s1 = input("Enter string1:")
s2 = input("Enter string2:")

s1 = s1.lower()
s2 = s2.lower()  # to get a and A as common character

a = len(s1)
b = len(s2)

for i in range(a):
    for j in range(b):
        if s1[i] == s2[j]:
            # error as , dsdhjas will print a s s i want single a s
            print(s1[i])


# Python Program to Count the Number of Vowels in a String.
string = input("Enter string:")
vowels = 0
string = string.lower()
for i in string:
    if i in "aeiou":
        vowels = vowels+1

print(f"number of vowels ={vowels}")
