#Find 33: Given a list of ints,return True if the array contains a 3 next to a 3 somewhere 
#has_33([1,3,3]) -->True        #list is passed as argument 
#has_33([1,3,1,3]) -->False
#has_33([3,1,3]) -->False

def has_33(mylist):
    i=0
    for item in mylist:
        if i==item :#as when i==item it will cause indexing error as i starts from 0 but item will iterate through 1 and goes till len(mylist)
            return False
        if mylist[i]==3 and mylist[i]==mylist[i+1]:
            return True
        else:
            i=i+1
    return False

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))