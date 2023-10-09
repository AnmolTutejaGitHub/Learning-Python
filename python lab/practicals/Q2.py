# a) Write a Python Program to Check if a Number is Odd or Even
n = int(input("Enter a number: "))
print("Number is even" if n % 2 == 0 else "Number is odd")

# b) Write a Python Program to Check if a Number is Positive, Negative or 0
num = float(input("Enter a number:"))

if num == 0:
    print("number is zero")
elif num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")

# c) Write a Python Program to Check Armstrong Number

# An Armstrong number (also known as a narcissistic number, pluperfect digital invariant,
# or pluperfect digital number) is a number that is equal to the sum of its own digits raised to the power of the number of digits.
# 153 is armstrong if 1^3 + 5^3 + 3^3 ==153

number = int(input("Enter a number:"))

number = str(number)
power = len(number)  # converted into str to find length
number = int(number)

numbercpy = number
cubicsum = 0
while number > 0:
    digit = number % 10
    cubicsum = cubicsum + (digit**power)
    number = number//10  # integer division

if cubicsum == numbercpy:
    print("isArmstrong")
else:
    print("It isn't")
