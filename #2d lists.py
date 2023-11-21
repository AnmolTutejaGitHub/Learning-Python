# 2d lists

# In Python, a 2D list is a list of lists, where each element in the outer list is a list itself. This creates a two-dimensional structure, similar to a matrix or a table. Each element in the inner lists represents an individual item, and the outer list organizes these inner lists.

# Here's a basic example of a 2D list in Python:

# Creating a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a 2D list
print(matrix[0])     # Output: [1, 2, 3]
print(matrix[1][1])   # Output: 5

# Modifying elements in a 2D list
matrix[1][2] = 10
print(matrix)
# Output:
# [
#     [1, 2, 3],
#     [4, 5, 10],
#     [7, 8, 9]
# ]

# Iterating through a 2D list
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
# Output:
# 1 2 3
# 4 5 10
# 7 8 9
# In the example above, matrix is a 3x3 matrix represented as a 2D list. You can access individual elements using indexing, and modify them as needed. The nested loops are used for iterating through the elements of the 2D list.

# Here are some common operations you can perform with 2D lists in Python:

# Creating a 2D List:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing Elements:

print(matrix[1][2])  # Accessing element in the second row, third column
# Modifying Elements:

matrix[0][1] = 10  # Modifying element in the first row, second column
# Iterating Through a 2D List:

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
# Adding a Row or Column:


matrix.append([10, 11, 12])  # Adding a row
for row in matrix:
    row.append(0)  # Adding an element to each row, effectively adding a column
# Deleting a Row or Column:
del matrix[1]  # Deleting the second row
for row in matrix:
    # Deleting the first element from each row, effectively deleting a column
    del row[0]
# These are just a few examples, and there are many other operations and techniques you can apply to 2D lists in Python.


# You can take input from the user to create a 2D list (matrix) using nested loops or list comprehensions. Here's an example using nested loops:


# Taking input for a 3x3 matrix
rows = 3
cols = 3

# Initialize an empty matrix
matrix = []

# Taking input from the user
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

# Displaying the matrix
print("Entered Matrix:")
for row in matrix:
    print(row)
# In this example, the program prompts the user to enter each element of the matrix. The outer loop (for i in range(rows)) iterates through the rows, and the inner loop (for j in range(cols)) iterates through the columns. The input is converted to an integer using int(input(...)) before appending it to the current row.

# You can modify the rows and cols variables to create a matrix of the desired size.

# Alternatively, you can use a list comprehension for a more concise solution:


# Taking input for a 3x3 matrix using list comprehension
rows = 3
cols = 3

matrix = [[int(input(f"Enter element at position ({i+1}, {j+1}): "))
           for j in range(cols)] for i in range(rows)]

# Displaying the matrix
print("Entered Matrix:")
for row in matrix:
    print(row)
# This achieves the same result as the nested loop example but in a more compact form using a list comprehension. The structure of the resulting matrix is the same in both cases.

# The eval() function in Python is a built-in function that parses and evaluates a Python expression (a piece of code) represented as a string. It takes a string as input, interprets it as a Python expression, and then executes the expression.

# While eval() can be powerful and flexible, it should be used with caution, especially when taking input from users, as it can execute arbitrary code. If used improperly, it may pose security risks.

# Here's an example of using eval() with the matrix input:


# Taking input for a 3x3 matrix using eval
rows = 3
cols = 3

matrix = [[eval(input(f"Enter element at position ({i+1}, {j+1}): "))
           for j in range(cols)] for i in range(rows)]

# Displaying the matrix
print("Entered Matrix:")
for row in matrix:
    print(row)
# In this example, the user is prompted to enter a Python expression for each matrix element. The eval() function then evaluates each entered expression. This allows the user to input not only simple values but also more complex expressions. For instance, the user can input 2 + 3 instead of just 5.

# However, it's important to note that using eval() with user input can be risky if the input is not properly validated. It opens the door to potential security vulnerabilities, as the user could input malicious code. If you're using eval(), make sure to validate and sanitize the input to ensure it's safe.

# In general, it's often safer and more predictable to use other methods for parsing and processing user input, especially if you don't need to evaluate arbitrary expressions. For numeric input, you can use int() or float() functions to convert input to integers or floats, respectively.


# A jagged list in Python is a list of lists where each inner list can have a different length. In contrast to a regular 2D list (matrix) where each row has the same number of elements, a jagged list allows for flexibility in terms of the length of each sub-list.

# Here's an example of a jagged list:

jagged_list = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
    [10]
]

# Accessing elements in a jagged list
print(jagged_list[0])     # Output: [1, 2, 3]
print(jagged_list[1][1])   # Output: 5
print(jagged_list[2][3])   # Output: 9

# Iterating through a jagged list
for row in jagged_list:
    for element in row:
        print(element, end=' ')
    print()
# Output:
# 1 2 3
# 4 5
# 6 7 8 9
# 10
# In this example, each inner list can have a different number of elements. You can access and manipulate elements in a jagged list in a similar way to a regular 2D list.

# Creating a jagged list is straightforward. You can create the outer list and then append inner lists with different lengths based on your requirements. For example:


jagged_list = []
jagged_list.append([1, 2, 3])
jagged_list.append([4, 5])
jagged_list.append([6, 7, 8, 9])
jagged_list.append([10])
# Jagged lists can be useful in situations where the data structure naturally has varying lengths for different components or when representing sparse data. Keep in mind that iterating through jagged lists might require handling the varying lengths appropriately in your code.


# To take a jagged list as input, you can use nested loops or list comprehensions to gather input for each sub-list. Here's an example using nested loops:


# Taking input for a jagged list using nested loops
rows = int(input("Enter the number of rows: "))

jagged_list = []
for i in range(rows):
    row_input = input(f"Enter space-separated elements for row {i + 1}: ")
    sub_list = [int(x) for x in row_input.split()]
    jagged_list.append(sub_list)

# Displaying the jagged list
print("Entered Jagged List:")
for row in jagged_list:
    print(row)
# In this example, the user is prompted to enter the number of rows, and then for each row, they input space-separated elements. The input is split into a list of strings using split(), and each string is converted to an integer using a list comprehension. The resulting list is then appended to the jagged list.

# You can also use a list comprehension for a more concise solution:


# Taking input for a jagged list using list comprehension
rows = int(input("Enter the number of rows: "))

jagged_list = [[int(x) for x in input(
    f"Enter space-separated elements for row {i + 1}: ").split()] for i in range(rows)]

# Displaying the jagged list
print("Entered Jagged List:")
for row in jagged_list:
    print(row)
# This achieves the same result as the nested loop example but in a more compact form using a list comprehension. The structure of the resulting jagged list is the same in both cases.
