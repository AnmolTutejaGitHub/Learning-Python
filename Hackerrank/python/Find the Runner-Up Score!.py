n=int(input())
# mylist=[]
# for i in range(n):  #taking input in this form so need to do comment out  a1,a2,a3,a4,
#     value=int(input())
#     mylist.append(value)
    
string=input()
mylist=string.split(" ")
int_list=[]
for item in mylist:
    int_list.append(int(item))
a=max(int_list)

secondlargest=-32000
for x in int_list:
    if x>secondlargest and x!=a:
        secondlargest=x
        
print(secondlargest)
