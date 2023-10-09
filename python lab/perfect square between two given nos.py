# perfect square between two given nos.
a = int(input())
b = int(input())

for i in range(a, b+1):
    sqrti = (i)**(1/2)
    if sqrti == int(sqrti):
        print(i)
