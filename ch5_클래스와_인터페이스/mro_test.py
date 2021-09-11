# class A:
#     def met(self):
#         print('A')
#         super().met()


# class B(A):
#     def met(self):
#         print('B')
#         super().met()


# class C(A):
#     def met(self):
#         print('C')
#         super().met()


# class D(B, C):
#     pass


# print(D.__mro__)
# d = D()
# d.met()


class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(A, B):
    pass


class E(C, D):  # 에러 발생!
    pass
