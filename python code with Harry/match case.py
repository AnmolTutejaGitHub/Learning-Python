# match case statement in python

x = int(input("value of x "))

# x is a variable to match
match x:
    case 0:
        print(" x is zero")
    case 4:
        print("x is four")
    case _:                 # _ is used for default
        print(x)

# in python jo case match hoga uska code run hoga there is no need of break statements
# can use if else in cases too
y = int(input("value of y "))

# x is a variable to match
match y:
    case 0:
        print(" y is zero")
    case 4:
        print("y is four")
    case _ if y != 90:                 # _ is used for default
        print(y, "y is not 90")
    case _ if y != 80:
        print(y, "y is not 80")
    case _:
        print(y, "y is not 90")


# jo case match ho gaya uske niche ke cases match nahi honge wahi pe break ho jayega
