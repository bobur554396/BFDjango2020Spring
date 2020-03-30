class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    def hello(self):
        print('class D')


d = D()

print(dir(d))
