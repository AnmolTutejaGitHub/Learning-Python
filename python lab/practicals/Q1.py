# a) Write a Python Program to Calculate the Area of a Triangle
h = float(input("Enter Height of the triangle(in m):"))
b = float(input("Enter Base of the triangle(in m):"))

area = (1/2)*b*h
print(f"Area of the triangle is {area} meter squares")

# b) Write a Python Program to Swap Two Variables
A = int(input("Enter first number (A):"))
B = int(input("Enter Second number (B):"))

# swapping logic
B = A+B
A = B-A
B = A-B
print(f"Swapped vales: A={A}, B={B}")

# c) Write a Python Program to Convert Celsius to Fahrenheit
celsius = float(input("Enter temperture in Celcius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in fahrenheit is {fahrenheit} degee fahrenheit")
