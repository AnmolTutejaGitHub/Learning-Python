#using global keyword

x=50

def func():  #dont pass x
    global x #functions can't change original value of x so use global keyword to change it outside the function through operations done by function
    print(f'X is {x}')

    x='new value'
    print(f'I just locally changed global X to {x}')

print(x)
func()
print(x)


#As a beginner U can use this methord instead:

y=50
def yfunc(y):
    print(f'Y is {y}')
    y='New value'
    print(f'I just changed Y to {y}')
    return y 

print(y)
y=yfunc(y) #@notice this 
print(y)

