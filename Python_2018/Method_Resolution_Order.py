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


d = D()
d.go()

# e = E()
# e.go()

