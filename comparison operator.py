# comparison operator

A=bool(2==2)
print(A)

B=bool("hello"=="bye")
print(B)

C=bool('2'==2)
print(C)
S=type(C)

x=2
y=2.0
z=bool(x==y) #returning True
print(z)

r=bool(1<2<3)
print(r)

w=bool(1<2>3)
print(w)       #False as 1<2 but 2 is not greater than 3





