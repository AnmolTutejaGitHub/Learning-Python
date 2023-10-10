# 1
# 01
# 101
# 0101
# 10101

n = int(input())

i = 1

while i <= n:
    j = 1
    while j <= i:
        if i % 2 == 0:
            logic = 1 if j % 2 == 0 else 0
        else:
            logic = 0 if j % 2 == 0 else 1
        print(logic, end="")
        j = j+1
    print()
    i = i+1
