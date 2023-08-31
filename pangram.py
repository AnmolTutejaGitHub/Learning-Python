# write a python function to check whether  a string is pangram or not(Assume the string passes in doesn't have any  punctuation)
#note: pangrams are  words or sentences containing every word orv alphabet at least once
#for example : "he quick brown fox jumps over the lazy dog"
#hint:youb wantv to use .replace method to get rid of spaces
#hint:look at the string module
#hint: in case you want to use set comparisons 

def pangram(s):
    mylist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=s.replace(' ','')
    s=s.lower()
    s= list(set(s))
    count=0
    print(s)
    for alphabet in mylist:
     a=mylist.index(alphabet) 
     for item in s:
        if item==mylist[a]:
           count=count+1
           break
    return count

if (pangram('The quick brown fox jumps over the lazy dog')) ==26:
   print("pangram")
else:
   print("Not")