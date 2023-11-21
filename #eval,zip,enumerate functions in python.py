# eval,zip,enumerate functions in python


# eval() Function:
# The eval() function in Python is used to evaluate a string as a Python expression. It takes a string as an argument and executes it as a Python expression. Here's a simple example:

expression = "2 + 3 * 4"
result = eval(expression)
print(result)  # Output: 14
# In this example, the string "2 + 3 * 4" is a mathematical expression, and eval() evaluates it, returning the result.

# It's important to use eval() cautiously, especially when dealing with user input, as it can execute arbitrary code and pose security risks if not used carefully.

# zip() Function:
# The zip() function in Python is used to combine elements from two or more iterables into tuples. It returns an iterator of tuples where the i-th tuple contains the i-th element from each of the input iterables. Here's an example:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
result = list(zipped)
print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# In this example, zip() combines elements from list1 and list2 into tuples.


# enumerate funtion

# The enumerate() function in Python is a built-in function that adds a counter to an iterable and returns it as an enumerate object, which is an iterator of pairs (index, element). This can be particularly useful when you need both the index and the value of elements in a loop.

fruits = ['apple', 'banana', 'orange']

for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")
# Output:

# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: orange
# In this example, enumerate(fruits) returns an enumerate object, and in the loop, index represents the index of the current element, and value represents the value of the current element.

# You can also specify a start value for the index by providing a second argument to enumerate(). For example:

fruits = ['apple', 'banana', 'orange']

for index, value in enumerate(fruits, start=1):
    print(f"Index: {index}, Value: {value}")
# Output:

# Index: 1, Value: apple
# Index: 2, Value: banana
# Index: 3, Value: orange
# Here, the enumeration starts from 1 instead of 0.

# The enumerate() function is commonly used in situations where you need to iterate over both the index and the value of elements in a sequence.
