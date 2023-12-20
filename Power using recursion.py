def myPow(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * myPow(x, n-1)


a = myPow(2, 5)
print(a)
