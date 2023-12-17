#Error handling
#Try,except,else,finally
def ask_for_int():
    while True:
        try:
            result=int(input("Enter a number: "))
        except:
            print("Whoops! that is not a number")
            continue
        else:
            print("Yes thank you")
            break #to break out of while loop
        finally:
            print("end of try,except,finally")
            print("I will run at end")

ask_for_int()

# else lets you code sections that should run only when no exceptions are encountered in the try clause.
try:
       # Some Code.... 
except:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no exception
finally:
      # Some code .....(always executed)
