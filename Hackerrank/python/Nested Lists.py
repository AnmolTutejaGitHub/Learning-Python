n=int(input())

arr=[]
namearr=[]
marksarr=[]
for i in range(n):
    name=input()
    namearr.append(name)
    marks=float(input())
    marksarr.append(marks)
    arr.append([name, marks])

lowest=float('inf')
secondlowest=float('inf')

for i in marksarr:
    if i<lowest:
        secondlowest=lowest
        lowest=i
    elif i<secondlowest and i!=lowest:
        secondlowest=i
    
#print(secondlowest)

finalList=[]
for i in range(len(namearr)):
    if marksarr[i] == secondlowest:
      finalList.append(namearr[i])
      
finalList.sort()
for i in finalList:
    print(i)
