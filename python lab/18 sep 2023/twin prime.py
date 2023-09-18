# Question 2: WAP to print twin primes less than 1000. 
# If two consecutive odd numbers are both prime then they are known as twin primes.

def isPrime():
    mylist=[]
    for j in range(2,1000):
     for i in range(2,j):
        if j%i!=0 and (j+1)%i!=0:
            mylist.append(j)
            mylist.append(j+1)

    print(mylist)

isPrime()