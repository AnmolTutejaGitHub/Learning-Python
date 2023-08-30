#SPY GAME: write a function that takes in a list of integers and returns True if it contains 007 in order.
#example:-
#spy_game([1,2,4,0,0,7,5])  True
#spy_game([1,0,2,4,0,5,7])  True
#spy_game([1,7,2,0,4,5,0])  False

def spy_game(mylist):
    a=10000    #so that I can use them in multiple for loops
    b=10000
    for item in mylist:
        if item==0:
            a=mylist.index(item)
            break
    i=0 #trace index of 2nd occurence of 0
    for item2 in mylist:
        if item2==0 and i>a and a!=10000:  #error as .index() always return index of 1st occurence 
           # b=mylist.index(item2)
            b=i
            break
        i=i+1
    for item3 in mylist:
         if item3==7 and mylist.index(item3)>b and a!=10000 and b!=10000:
                 return True
         
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))            