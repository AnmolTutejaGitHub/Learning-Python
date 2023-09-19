# Question 2: WAP to print twin primes less than 1000. 
# If two consecutive odd numbers are both prime then they are known as twin primes.
def isPrime(n):
    prime=True
    for _ in range(2,n):
        if n%_==0:
            prime =False

    return prime  

for _ in range(3,1000):
    if isPrime(_) and isPrime(_+2):
        print(_,_+2)
    else:
        pass

