# sorted vs sort in python 

# In Python, both sorted() and sort() are used for sorting elements in a sequence, but they are used in slightly different contexts.

# sorted() Function:

# sorted() is a built-in function in Python that returns a new sorted list from the elements of any iterable (e.g., list, tuple, string).
# It does not modify the original iterable; instead, it creates a new sorted list.
# The syntax is: sorted(iterable, key=None, reverse=False)
# iterable: The sequence to sort.
# key: A function to extract a comparison key from each element (optional).
# reverse: If True, the list is sorted in descending order (optional).
# Example:

original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(original_list)
print(sorted_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
list.sort() Method:

# sort() is a method that belongs to the list data type in Python.
# It modifies the list in-place, meaning it rearranges the elements of the original list.
# The syntax is: list.sort(key=None, reverse=False)
# key: A function to extract a comparison key from each element (optional).
# reverse: If True, the list is sorted in descending order (optional).
# Example:

original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
original_list.sort()
print(original_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
# In summary, use sorted() when you want to create a new sorted list without modifying the original, and use sort() when you want to sort a list in-place. The choice depends on your specific requirements and whether you need to preserve the original order of the elements.


# Both sorted() and str.sort() can be used to sort strings according to ASCII order in Python.

# Using sorted() with Strings:
original_string = "hello"
sorted_string = ''.join(sorted(original_string))
print(sorted_string)  # Output: "ehllo"
# The sorted() function is used to create a sorted list of characters from the original string, and then ''.join() is used to concatenate them back into a string.



# Using str.sort() with Lists of Characters:
original_string = "hello"
char_list = list(original_string)
char_list.sort()
sorted_string = ''.join(char_list)
print(sorted_string)  # Output: "ehllo"
# Here, the string is converted to a list of characters, which is then sorted in-place using the sort() method, and finally, ''.join() is used to create a string from the sorted list.

# Both approaches will result in the characters being sorted according to their ASCII values. 
