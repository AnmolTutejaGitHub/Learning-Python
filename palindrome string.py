#write  a  python function that checks whether a word or phrase is palindrome or not
#hint: "madam" is palindrome . "nurses run" is also palindrome
#you may want to check out .replce() in a string to help out with dealing with spaces
#there are clever ways to reverse a string with slicing notation

def palindrome(s):
    #remove spaces in string
    s=s.replace(" ","")
    #check is string==reversed version of the string
    return s==s[::-1]

print(palindrome("nurses run"))