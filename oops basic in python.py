# oops in python syntax

class NameofClass():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some actiom
        print(self.param1)


# creating instance of the class
anmol = NameofClass('anmol', 'tuteja')
anmol.some_method()  # anmol

print(type(anmol))  # <class '__main__.NameofClass'>


# Attributes

class Dog():
    def __init__(self, breed):

        # attribues

        self.breed = breed
        # can also do
        self.example = breed


my_dog = Dog(breed="lab")

print(my_dog.breed)  # lab
print(my_dog.example)  # lab


# class object attribute
class DogSpecies():
    # class object attribute
    # same for any instance of a class
    # so  we don't use self keyword as self keyword is reference to  a particular instance of a class

    species = 'mamal'

    def __init__(self, breed):
        self.breed = breed

    # methods

    def bark(self):
        print("woof!")


Tom = DogSpecies("Labra")

print(Tom.species)  # mamal
print(Tom.breed)  # Labra

Tom.bark()  # woof!
# <bound method DogSpecies.bark of <__main__.DogSpecies object at 0x100875790>>
print(Tom.bark)


# Methods

class programmer():
    species = 'Humans'

    def __init__(self, name, language):
        self.name = name
        self.language = language

    # methods

    # we pass self keyword as we need to reference particular instance of name/language
    def speciality(self, profession):  # can pass external arguments eg in this case profession
        print(
            f"My name is {self.name} and I have  a good knowledge of {self.language} and I am working as {profession}")  # no need to pass name or self.name in method parameters as they are declared in class declaration


jack = programmer(language="java", name="jack")

print(jack.name)  # jack
# My name is jack and I have  a good knowledge of java and I am working as CTO
jack.speciality("CTO")

# jack.speciality() will give error if i pass external argument in method and didnt pass here


# can provide default values

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        # can also do this :
        # can also do Circle.pi #for class level attributes
        self.area = radius*radius*self.pi
        # both will work correct
        # self.area = self.radius*self.radius*self.pi

    def get_circumference(self):
        return self.radius*self.pi*2  # note self.pi


my_circle = Circle()  # now default radius is set

print(my_circle.radius)  # 1


my_circle2 = Circle(2)
print(my_circle2.radius)  # 2

print(my_circle2.area)  # 12.56


# inheritance : A way to form new classes using classes that  have already been defined


# base class
class Animal():
    def __init__(self):
        print("Animal created")

    def eat(self):
        print("Animal is eating")


# Animal created    #as init method will be called on every class declaration
myAnimal = Animal()


# creating child class
class dog(Animal):  # passing base class name
    def __init__(self):
        Animal.__init__(self)  # linking self
        # I created instance of animal class when I created an instance of dog class

        # can ovwerWrite methods

    def eat(self):
        print("Dog is eating")


# polymorphism  (later)


# normal methods/funtions give diffrent result on classes as:

# special methods

class book():
    def __init__(self, name, title, author):
        self.name = name
        self.title = title
        self.author = author


b = book("Humans", "they still exist", "God")
# print(b)  # <__main__.book object at 0x10516c210><__main__.book object at 0x10516c210>
# print(len(b))  # TypeError: object of type 'book' has no len())


# using special methods we can make these methods work on my class
class book2():
    def __init__(self, name, title, author, pages):
        self.name = name
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # this is occur if somewhere str repesentation of this class is asked  note print ask for str representation
        return f"{self.name} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        return "object has been deleted"


b2 = book2("Humans", "wasted 7 days of my life", "God", 69)

print(b2)  # Humans by God
print(len(b2))  # 69
del b2
