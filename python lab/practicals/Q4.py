# a.) Write a Python Program to Print Pascal Triangle
# Hint: Enter number of rows: 4
#                   1
#                1      1
#             1      2      1
#          1      3      3      1

def generate_pascal_triangle(n):
    result = []
    for i in range(n):
        row = [1]
        if result:
            last_row = result[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        result.append(row)
    return result


num_rows = int(input("Enter number of rows: "))
pascal = generate_pascal_triangle(num_rows)

# Print Pascal's Triangle
for i in range(num_rows):
    print("   " * (num_rows - i), end="")
    for j in pascal[i]:
        print(j, end="      ")
    print()


# b.) WAP to Draw the following Pattern for n number:
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

n = int(input("Enter n:"))

i = 1
while i <= n:
    j = 1
    while j <= n-i+1:
        print(i, end='')
        j = j+1
    print()
    i = i+1
