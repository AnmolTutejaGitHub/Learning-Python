# a) Write a Python program to check if a given number is Fibonacci number?
# To check if a given number is a Fibonacci number, you can use the properties of Fibonacci numbers.
# A number is a Fibonacci number if and only if one of the expressions (5 * n^2 + 4) or (5 * n^2 - 4) is a perfect square.
# a perfect square is a number that is the square of an integer.
n = int(input("Enter a number:"))

a = 5 * n**2 + 4
b = 5 * n**2 - 4

# checking perfect square (square root nikal ke integer form se compare karna if 2.5 hai sqrt then int(2.5) is 2 so not fibocaai)
sqrta = (a)**(1/2)
sqrtb = (b)**(1/2)

if sqrta == int(sqrta) or sqrtb == int(sqrtb):
    print("is a fibonacci number")
else:
    print("is not!")


# b) Write a Python program to print cube sum of first n natural numbers.

def cube_sum(n):
    if n == 0:
        return 0
    else:
        return n**3 + cube_sum(n-1)


num = int(input("Enter the value of n: "))

cube_sum_result = cube_sum(num)

print(f"Cube sum of the first {num} natural numbers is {cube_sum_result}")

# c) Write a Python program to print all odd numbers in a range.
start = int(input("Enter starting value of the range:"))
end = int(input("Enter ending value of the range:"))

for i in range(start, end+1):
    if i % 2 != 0:
        print(i)
