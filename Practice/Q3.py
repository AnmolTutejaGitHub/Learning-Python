# Kirti has been asked to give a sentence in the form of a string as a function parameter. The task
# is to print the sentence such that each word in the sentence is reversed.
# Input Format:
# The only line of input contains a string that represents the sentence given by Kirti.
# Output Format:
# The only line of output prints the sentence such that each word in the sentence is reversed.
# Constraints:
# 0 <= N <= 100
# Where N is the length of the input string.
# Sample Input 1:
# Welcome To Chitkara
# Sample Output 1:
# emocleW oT araktihC
# Solution:
# def rev_sentence(sentence):
# words = sentence.split(" ")
# new_words = [word[::-1] for word in words]
# new_sentence = " ".join(new_words)
# return new_sentence
# sentence = input()
# print(rev_sentence(sentence))
# TestCase1 Hello World! olleH !dlroW
# TestCase2 Jai Hind iaJ dniH
# TestCase3 Well Done lleW enoD
# TestCase4 Super Star repuS ratS
# TestCase5 Day Night yaD thgiN

s = input()
strlist = s.split(' ')
reversed = ""
for i in strlist:
    if reversed == "":
        reversed += i[::-1]
    else:
        reversed += ' '+i[::-1]

print(reversed)
