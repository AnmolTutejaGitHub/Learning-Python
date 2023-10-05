# 1
# 12
# 123
# 1234

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j = j+1
    print()
    i = i+1
