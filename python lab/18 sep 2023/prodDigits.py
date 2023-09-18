def prodDigits(n):
    len(n)
    product=1
    for _ in range(1,len(n)+1):
     n=int(n)
     var = n%10
     product=product*var
     n=int(n/10)
    return product

number=(input("Enter Number:"))
print(prodDigits(number))