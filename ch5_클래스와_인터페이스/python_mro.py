class A:
    def met(self):
        print('A')


class B(A):
    def met(self):
        print('B')


class C(A):
    def met(self):
        print('C')


class D(B, C):
    def met(self):
        print('D')


print(D.__mro__)
d = D()
d.met()

print("="*30)


class A:
    def met(self):
        print('A')


class B(A):
    def met(self):
        print('B')


class C(A):
    def met(self):
        print('C')


class D(B, C):
    pass


print(D.__mro__)
d = D()
d.met()
print("="*30)


class A:
    def met(self):
        print('A')


class B(A):
    def met(self):
        print('B')
        super().met()


class C(A):
    def met(self):
        print('C')


class D(B, C):
    pass


print(D.__mro__)
d = D()
d.met()
print("="*30)


# 교차된 순서로 부모에게 상속받을 떄 에러
# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class D(B, A):
#     pass

# class E(C, D): # 에러 발생!
#     pass
