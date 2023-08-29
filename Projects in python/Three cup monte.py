#Three cup monte
from random import shuffle

n=1
while n==1:
 my_cups=['cup1','cup2','cup3']
 myball=my_cups[0]

 user = int(input("Enter cup number in which you think the ball is present (strictly advised to use 1, 2, 3 integers only):"))
 
 if user!=1 and user!=2 and user!=3:
   print("U dont know how to play!")
   n=0

 else:
   pass

 shuffle(my_cups)

 if my_cups[user-1]==myball:
  print('U win')
  n=0
 else:
   print("Wrong answer")
   n=1





   



