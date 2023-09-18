#functions practice questions - 1

# Question 1: WAP that iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number 
# and for multiples of five print "Buzz". 
# For numbers that are multiples of three and five, print "FizzBuzz".

for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else :
        print(num)


# Question2: Program to print the alphabet pattern 'A'.

# Question 3: program to check whether an alphabet is a vowel or consonant.
#List of alphabets
#alphalist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowel=['a','e','i','o','u']
var=input("Enter an alphabet: ")

if var.lower() in vowel:
    print("vowel")
else :
    print("consonent")


# Question 4: WAP to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal
# to 10.5 human years. After that, each dog year equals 4 human years.

dogAge=int(input("Enter Dog's Age:"))

if dogAge==2:
    dogYear=10.5
elif dogAge>2:
    dogYear=10.5+4*(dogAge-2)
  
print(f"Dog's age in Dog's Years = {dogYear}")


#Question 5: program that checks whether a string represents an integer or not.
def funct(string):

    print(string.isdigit())

s=input("Enter a string:")
funct(s)

# FUNCTIONS: Question1: Write a function that inputs a number and 
# prints the multiplication table of that number.
def func(number):

    for _ in range(1,11):
        print(number*_)

number=int(input("Enter a number:"))
func(number)




# Question 2: WAP to print twin primes less than 1000. 
# If two consecutive odd numbers are both prime then they are known as twin primes.

# def isPrime():
#     mylist=[]
#     for j in range(2,1000):
#      for i in range(2,j):
#         if j%i!=0 and (j+1)%i!=0:
#             mylist.append(j)
#             mylist.append(j+1)

#     print(mylist)

# isPrime()
    
#Write a function cubesum() that accepts an integer and returns the sum of the cubes 
# of individual digits of that number. Use this function to make functions 
# PrintArmstrong() and isArmstrong() to print Armstrong numbers and to find 
# whether is an Armstrong number.




#Question 4: WAP prodDigits() that inputs a number and returns the product of 
# digits of that number.
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



