#pangram or not
#another method
import string
def ispangram(str1,alphabet=string.ascii_lowercase):
    #create a set of the alphabet
    alphaset=set(alphabet)
    #remove any spaces from input string
    str1=str1.replace(" ","")
    #convert into all lowercase
    str1=str1.lower()
    #grab all unique letters from string set()
    str1= set(str1)
    # alphabet set == string set input
    return str1==alphaset

print(ispangram("The quick brown fox jumps over the lazy dog"))