#Python oddies: round function wired case
#Gaussian rounding : rounds halves to near even number
#why : [1.5,2.5,0.5,1] total sum=5.5
#rounds up :sum= 2+3+1+1=7   error=1.5
#rounds down :sum=1+2+0+1=4  error=1.5
#Gaussian rounding: sum= 2+2+0+1=5  error=0.5
#python round function follows gaussian rounding 

a=round(3.5)
print(a)

b=round(4.5)
print(b)

c=round(7.5)
d=round(8.5)
print(c,d)




