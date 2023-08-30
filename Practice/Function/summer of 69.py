#Summer of '69: Return the sum of the numbers in the array,except ignore sections of numbers starting with a 6
#and extending to the next 9(every 6 will be followed by at least one 9).Return 0 for no numbers.
#example: 
#summer_69([1,3,5]) --> 9
#summer_69([4,5,6,7,8,9]) --> 9
#summer_69([2,1,6,9,11]) --> 14



#######
    #     MY CODE NOT WORKING 
                               #######

def summer_69(mylist):
    found=0
    for item in mylist:
        if item==6:
            found=1
            a=mylist.index(item)

            for item2 in mylist:
             if found==1 and item2==9:
              b=mylist.index(item2)
              return sum(mylist)-sum(mylist[a:b])
    
    return sum(mylist)
        
print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8]))
print(summer_69([2,1,6,9,11]))

