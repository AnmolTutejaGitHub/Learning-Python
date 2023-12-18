n=int(input())
arrStr=input()
arr=arrStr.split(' ')

dict={}

for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
            dict[i]=count
            
sum=0
for key, value in dict.items():
    sum+=value//2
    
print(sum)
    
