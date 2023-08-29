#kwargs arguments
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I didn't find any fruit")

myfunc(fruit='apple', veggie='lettuce')

def func(*args, **kwargs):
    print("I Would like {}{}".format(args[0], kwargs['food']))

func(10, 20, 30, fruit='orange', food='eggs', animal='dog')
