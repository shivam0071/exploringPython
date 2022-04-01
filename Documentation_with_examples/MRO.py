# Python program to show the order
# in which methods are resolved
# Depth First Left to Right, New Approach uses C3 Linearization  Algorithm
class A:
    def display(self):
        print(" In class A")


class B:
    def display(self):
        print(" In class B")


# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")


r = C()
# it prints the lookup order 
print(C.__mro__)
print(C.mro())


class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()

print(D.__mro__)
print(D.mro())