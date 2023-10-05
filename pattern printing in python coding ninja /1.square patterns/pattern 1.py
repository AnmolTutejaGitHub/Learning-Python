# ****
# ****
# ****
# ****

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        # if end not specified by default python will end with new line
        print("*", end='')
        j = j+1
    print()  # for new line
    i = i+1
