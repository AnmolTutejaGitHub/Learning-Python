#ANIMAL CRACKERS: Write a function takes a two word string and returns True if both words begin with same letter

def myfunc(string):
    list_string=string.split()
    # for i in list_string:   #string.split() returns list
    #     string1=list_string[0]
    #     string2=list_string[1]
    
    if list_string[0][0]==list_string[1][0]:  #list_string[0]=1st element of list
        return True
    else:
        return False

print(myfunc("anmol json"))




