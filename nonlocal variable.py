# non local variable
# In Python, non-local variables are variables that are defined in an enclosing function but are not global.
# They are used when you want to modify a variable that is in an outer (enclosing) function's scope, but you don't want to make it a global variable.

# Here's an example to illustrate non-local variables in Python:
def outer_function():
    x = 10  # This is a variable in the enclosing function

    def inner_function():
        nonlocal x  # Declare x as a non-local variable
        x += 5  # Modify the non-local variable

    inner_function()
    print("Modified x:", x)


outer_function()

# In this example, the x variable is defined in the outer_function. We want to modify this variable from within the inner_function.
# To do this, we use the nonlocal keyword to indicate that x is not a local variable of inner_function but a variable in the enclosing outer_function.
#  Then, we can modify x within inner_function.

# Output:Modified x: 15
# Without using nonlocal, modifying x would create a new local variable within inner_function rather than modifying the variable in the enclosing scope.
# The use of nonlocal allows us to modify the variable in the enclosing scope.













