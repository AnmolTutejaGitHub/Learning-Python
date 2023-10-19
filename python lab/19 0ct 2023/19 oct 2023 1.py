# 1. Write a program that accepts a string from user. Your program should count and display number of vowels in that string.
s = input("Enter a string : ").lower()

vowel = 0
vow = ["a", "e", "i", "o", "u"]
for i in s:
    if i in vow:
        vowel = vowel+1

print(f"no. of vowels ={vowel}")

# Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string
lower = 0
upper = 0
digits = 0
digarr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
whitespace = 0
for i in s:
    if i == i.lower():
        lower = lower+1
    if i == i.upper():
        upper = upper+1
    if i == " ":
        whitespace = whitespace+1
    if i in digarr:
        digits = digits+1

print(
    f"vowels={vowel},upper={upper},lower={lower},whitespace={whitespace},digits={digits}")

# 3. Write a Python program that accepts a string from user. Your program should create and display a new string where the first and last characters have been exchanged.

# For example if the user enters the string 'HELLO' then new string would be 'OELLH'

str = input("Enter a string: ")
end = len(str)

print(str[-1]+str[1: end]+str[0])

# 4.Write a Python program that accepts a string from user. Your program should create a new string in reverse of first string and display it.

# For example if the user enters the string 'EXAM' then new string would be 'MAXE'
print(s[::-1])
