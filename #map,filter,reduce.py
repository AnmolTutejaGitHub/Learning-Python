# map,filter,reduce
# map, filter, and reduce are three built-in functions in Python that operate on sequences (such as lists) and are often used in functional programming.

# map function:

# The map function applies a given function to all items in an iterable (e.g., a list) and returns an iterable of the results.

# Example: Squaring each element in a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
# In this example, the map function applies the lambda function (which squares each element) to each item in the numbers list.

# filter function:

# The filter function constructs a new iterable from elements of the iterable for which a function returns True.

# Example: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8]
# In this example, the filter function retains only the elements in the numbers list that satisfy the condition of being even.

# reduce function:

# The reduce function is part of the functools module (in Python 3) and successively applies a binary function to the items of an iterable, reducing them to a single accumulated result.


# Example: Summing up all elements in a list
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15
# In this example, the reduce function applies the lambda function (which adds two numbers) successively to the elements of the numbers list, resulting in the sum of all elements.

# Note: In Python 3, reduce was moved to the functools module, so you need to import it explicitly.

# These functions provide a concise and expressive way to perform common operations on sequences in a functional style.


#  The reduce function is used to successively apply a binary function to the items of an iterable, reducing them to a single accumulated result. The general syntax is:


# result = reduce(function, iterable[, initializer])


# function: The binary function to apply successively to the items of the iterable. It should take two arguments.
# iterable: The iterable (e.g., a list) whose elements will be successively combined.
# initializer (optional): An optional initial value. If provided, it is placed before the items of the iterable in the calculation, and the function is applied to the result and the next item in the iterable.
# Here's an example of using reduce to find the product of all elements in a list:


numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
# In this example, the lambda function takes two arguments (x and y) and returns their product. The reduce function applies this lambda function successively to the elements of the numbers list, resulting in the product of all elements.

# You can also provide an optional initializer. For example, finding the product with an initial value of 1:


# from functools import reduce

numbers = [2, 3, 4, 5]
product_with_initializer = reduce(lambda x, y: x * y, numbers, 1)
print(product_with_initializer)  # Output: 120
# In this case, the initial value of 1 is multiplied by the elements in the list. If the list were empty, the result would be the initializer (1 in this case).

# Remember that using reduce can sometimes make code less readable, so it's often preferable to use built-in functions like sum, min, or max for specific reduction tasks.
