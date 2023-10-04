# reversing a number

num = int(input())
rem = 0

while num > 0:
    rem = rem*10+num % 10
    # upd=rem
    num = num//10
print(rem)
