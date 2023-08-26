from random import randint
from os import remove
n=1
while n==1:
 num=int(input("Enter a number(0-100):"))
 if num>=100 and num<=0:
   n=0
   pass
 else:
    print("\nDo it again")
    n=1

comnum=randint(0,100)
if num==comnum:
   print("U!won")
#else :
#  remove("C:\windows\system32")
