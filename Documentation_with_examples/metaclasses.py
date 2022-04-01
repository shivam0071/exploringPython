# Usage
# one of the use of metaclasses is to control the behaviour of the derived classes from base class when
# base class has no idea who will inherit it.

#  For example if Base class wants all the derived classes to have a common function say FOO
# then we can achieve this by using metaclasses.

# NOTE
# A derived class can make sure that a function that the are calling in the Base class is present or not
# is by using assert... assert hasattr(BaseClass, 'Function_name')


# USING HOOKS
class BaseMeta(type):

    def __new__(cls, name, base, body):
        # name is name of the class inheriting BaseMeta
        # base what is the base class
        # body is a dict of attributes given below
        print(body)
        # We can see that we have function names in body
        # {'__module__': '__main__', '__qualname__': 'Base', 'foo': <function Base.foo at 0x0000027C3AD3A9D0>}
        # {'__module__': '__main__', '__qualname__': 'Derived', 'bar': <function Derived.bar at 0x0000027C3AD3AA60>}

        if name != 'Base' and 'bar' not in body:
            raise TypeError("Bad User Class")

        return super().__new__(cls, name, base, body)

class Base(metaclass=BaseMeta):

    def foo(self):
        return self.bar()

class Derived(Base):

    def bar(self):
        return 'Bar'


b = Derived()
print(b.foo())


#  ANOTHER WAY OF DOING THIS is by using __init_subclass__() dunder

class BaseMeta(type):

    def __new__(cls, name, base, body):
        # name is name of the class inheriting BaseMeta
        # base what is the base class
        # body is a dict of attributes given below
        print(body)
        # We can see that we have function names in body
        # {'__module__': '__main__', '__qualname__': 'Base', 'foo': <function Base.foo at 0x0000027C3AD3A9D0>}
        # {'__module__': '__main__', '__qualname__': 'Derived', 'bar': <function Derived.bar at 0x0000027C3AD3AA60>}

        if name != 'Base' and 'bar' not in body:
            raise TypeError("Bad User Class")

        return super().__new__(cls, name, base, body)

class Base(metaclass=BaseMeta):

    def foo(self):
        return self.bar()

    def __init_subclass__(cls, **kwargs):
        print("INIT SUBCLASS", **kwargs)
        return super().__init_subclass__(**kwargs)


class Derived(Base):

    def bar(self):
        return 'Bar'



# USING TYPE - type('',(), {}) .. class name, bases(base classes), body - class variables and funcitons
def howdy(self, me):
    print("Howdy, " + me)

MyList = type('MyList', (list,), dict(y=12, howdy=howdy))
ml = MyList()
ml.append("John")
print(ml)