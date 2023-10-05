# Que 8,9 left
# 1234
# 123
# 12
# 1

n = int(input())
i = n
while i <= n and i > 0:
    # i = 1
    j = 1
    while j <= i:
        print(j, end='')
        j = j+1
    print()
    i = i-1

# for this que I was doing j=j-1  and j=i ib]nstead of i=n when u look carefully u need to do i=i-1
