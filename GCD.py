#calculating GCD of two nos.

a=int(input())
b=int(input())
f=1
i=1
min = a if a<b else b #ternary operator
min_v=int(min)
for i in range(1,min_v +1):
  if a%i==0 and b%i==0 :
    f=i

print(f)
