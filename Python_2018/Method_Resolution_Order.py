# https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path

class A:
    def go(self):
        print('Inside A')

class B(A):
    def go(self):
        print('B')
        # super(B,self).go()
        super().go()
        print('Inside B')


class C(A):
    def go(self):
        print('C')
        # super(C, self).go()
        super().go()
        print('Inside C')

class D(B,C):
    def go(self):
        print('D')
        # super(D, self).go()
        super().go()
        print('Inside D')

class E(B,C):
    pass


# d = D()
# d.go()
#
# e = E()
# e.go()

# D
# B
# C
# Inside A
# Inside C
# Inside B
# Inside D


class X():
    def who_am_i(self):
        print("I am a X")


class Y():
    def who_am_i(self):
        print("I am a Y")


class A(Y, X):
    # def who_am_i(self):
    #     print("I am a A")
    pass


class B(X):
    # def who_am_i(self):
    #     print("I am a B")
    pass


class F(A, B):
    # def who_am_i(self):
    #     print("I am a F")
    pass

f = F()
f.who_am_i()

# Left to right ...deep in
# I am a F
# I am a A
# I am a B
