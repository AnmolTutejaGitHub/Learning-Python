# 1
# 21
# 321
# 4321

n = int(input())
i = 1
while i <= n:
    k = i
    j = 1
    while j <= i:
        print(k, end='')
        j = j+1
        k = k-1
    print()

    i = i+1
