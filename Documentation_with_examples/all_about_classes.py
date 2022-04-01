
class Student:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name = name   # private instance attribute
        self.__salary = age  # private instance attribute

    def __display(self):  # private method
        print('This is private method.')


sss = Student("Sss", 23)


from abc import ABC, abstractmethod

class abstract_demo(ABC):

    def __init__(self):
        print("INIT")

    @abstractmethod
    def demo(self):
        pass

# abs = abstract_demo()

# Static Methods
class Dog:
    count = 0  #static vars
    dogs = []

    def __init__(self, name):
        self.name = name
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self):
        print('grrrrrrrrrrrr...woof woof')
        print(Dog.dogs)

    def rollback():                 #Static method made implicitly
        print(Dog.count, Dog.dogs)

    @staticmethod                   #Static method made explicitly
    def jump():
        print(Dog.count, Dog.dogs)
        print("JUMP")

scrappy = Dog("Scrappy")
tommy = Dog("Tommy")
tommy.bark()
Dog.rollback() #calling static methods, unable to call from instance tommy
Dog.jump()      # calling static methods
tommy.jump()    #also unable to call from instance tommy

# Class Methods + Alternate constructor
class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
        # Recall that Python allows multiple variable assignments in one line
        self.year, self.month, self.day = year, month, day

    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)


bd = BetterDate.from_str('2020-04-30')
print(bd.year)
print(bd.month)
print(bd.day)


# Python program to illustrate the use of
# @property decorator

# Defining class
class Portal:

    # Defining __init__ method
    def __init__(self):
        self.__name = ''

    # Using @property decorator
    @property
    # Getter method
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val

    # Deleter method
    @name.deleter
    def name(self):
        del self.__name


# Creating object
p = Portal()

# Setting name
p.name = 'Some String'

# Prints name
print(p.name)
#
# Deletes name
# del p.name
#
# # As name is deleted above this
# # will throw an error
# print(p.name)


# BEFORE __INIT__
# Use __new__ when you need to control the creation of a new instance.
# __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
class A(object):
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)

    def __init__(self):
        print("Init is called")

A()

# SINGLTON DECORATOR

def singleton(cls):
    instances = {}
    def getinstance(*args):
        if cls not in instances:
            instances[cls] = cls(*args)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

my = MyClass('Dummy')
my.display()
# Trying to create a new object just returns old object
my2 = MyClass('Dummy2')
my.display()


# USING SUPER
class using_super:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        # some common implementations (optional)
        print(self.name)


class using_super_child(using_super):

    def display(self):
        super().display()
        # Extending functionality
        print("My nick name is Hobo")

child= using_super_child('Bablu')
child.display()