n=int(input())

def printer(n):
    mylist=[]
    for num in range(1,n+1):
        mylist.append(str(num)) #as join function expects a list of str to join
        
    string="".join(mylist)
    print(string)
    
    
printer(n)
