# fibonachi series:
A = 0
B = 1
if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
else:
    for i in range(2, n):
        C = A+B
        # A = B  # swapping like logic 
        # B = C
        A, B = B, C   #python specific
        print(C)
