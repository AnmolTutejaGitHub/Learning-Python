#Paper doll: Given a string,return where for every character in the original there are 3 characters
#example:
#paper_doll('Hello') -->'HHHeeellllllooo'

def paper_doll(string):
    i=0
    list_ch_by_ch=list(string)  #convert string into list, elements are character by character
    anotherlist=[] 
    x=3*len(list_ch_by_ch)       #can avoid this 
    for item in range(0,x,3):    #simply do range(0,len(list_ch_by_ch))  #no need of jump now 
           anotherlist.append(list_ch_by_ch[i]+list_ch_by_ch[i]+list_ch_by_ch[i])
           i=i+1

    anotherstring=''.join(anotherlist)
    return anotherstring

print(paper_doll("Hello"))