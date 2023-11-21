# Exception handling in python
# Exception handling with try, except, else, and finally
# Try: This block will test the excepted error to occur
# Except:  Here you can handle the error
# Else: If there is no exception then this block will be executed
# Finally: Finally block always gets executed either exception is generated or not
# Python Try, Except, else and Finally Syntax
# try:
#        # Some Code....
# except:
#        # optional block
#        # Handling of exception (if required)
# else:
#        # execute if no exception
# finally:
#       # Some code .....(always executed)

# Example:

# Python code to illustrate working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

# Here’s an example that demonstrates how to use multiple except clauses to handle different exceptions:

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")


Else Clauses in Python
The code enters the else block only if the try clause does not raise an exception.

# Example: Else block will execute only when no exception occurs.


# Python code to illustrate working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)


# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

# Output:

# Yeah ! Your answer is : 1
# Sorry ! You are dividing by zero


# Python finally Keyword
# Python provides a keyword finally, which is always executed after try and except blocks. The finally block always executes after normal termination of try block or after try block terminates due to some exception. Even if you return in the except block still the finally block will execute

# Example: Let’s try to throw the exception in except block and Finally will execute either exception will generate or not


# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')


# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)
Output:

    # Yeah ! Your answer is : 1
    # This is always executed
    # Sorry ! You are dividing by zero
    # This is always executed

    # we #Error handling
    # Try,except,else,finally


def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number: "))
        except:  # now it handles all errors
            print("Whoops! that is not a number")
            continue
        else:
            # why in else part not with try because it will then be excuted with try
            print("Yes thank you")
            break  # to break out of while loop
        finally:
            print("end of try,except,finally")
            print("I will run at end")


ask_for_int()
