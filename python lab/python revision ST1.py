# python revision
a = 0.98
print(type(a))


b = "hello"
print(b.upper())


# spilt
c = "hello my name is Anmol"
print(c.split())
print(c.split("n"))


print("The {} {} {}".format('fox', 'brown', 'quick'))
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))
print("The {f} {q} {f}".format(f='fox', q='brown', g='quick'))

name = 'jose'
print(f"hello my name is {name}")


# fibonacci series
# nth member of fibocaai series

n = int(input())


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


output = fibonacci(n-1)
print(output)


# # fibocaai series


# for i in range(2, n+2):  # 2 as i want to use i for indexing
#         fval = f[i-1]+f[i-2]  # here
#         f.append(fval)


# print(f)


# fibonachi series:
A = 0
B = 1
if n == 1:
    print(A)
elif n == 2:
    print(A)
    print(B)
else:
    print(A)
    print(B)
    for i in range(2, n):
        C = A+B
        # A = B  # swapping like logic
        # B = C
        A, B = B, C  # python specific
        print(C)


# reversing a number

num = int(input())
rem = 0

while num > 0:
    rem = rem*10+num % 10
    # upd=rem
    num = num//10
print(rem)


##