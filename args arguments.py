# *args argument

def my_func(*args):  #takes input in form of Touple
    print(args)
    print (sum(args))

my_func(10,23,56,87)


def func(*args):
    for item in args:
        print(item)

func('anmol',1,'Tuteja',111)

#can also do
def funct(*spam):
    for item in spam:
        print(spam)

funct('Anmol',1,'r2')