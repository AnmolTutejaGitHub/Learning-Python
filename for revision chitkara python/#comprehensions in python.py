#comprehensions in python
# List Comprehension:
squares = [x**2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary Comprehension:
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# Set Comprehension:
squares_set = {x**2 for x in range(10)}
print(squares_set)
# Output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}


# Tuple Comprehension (Note: There's no direct tuple comprehension, but you can use a generator expression and convert it to a tuple):
# Create a tuple of squares for numbers from 0 to 9
squares_tuple = tuple(x**2 for x in range(10))
print(squares_tuple)
# Output: (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

# String Comprehension (Using a list comprehension to join characters into a string):

# Create a string of even numbers from 0 to 9
even_numbers_string = ''.join(str(x) for x in range(10) if x % 2 == 0)
print(even_numbers_string)
# Output: '02468'
