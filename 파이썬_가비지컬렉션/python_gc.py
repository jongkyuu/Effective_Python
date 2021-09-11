# import sys


# class RefenceCountTest():
#     def __init__(self):
#         print('create object')


# a = RefenceCountTest()
# print(f'count {sys.getrefcount(a)}')
# b = a
# print(f'count {sys.getrefcount(a)}')
# c = a
# print(f'count {sys.getrefcount(a)}')
# c = 0
# print(f'count {sys.getrefcount(a)}')
# b = 0
# print(f'count {sys.getrefcount(a)}')

# """
# OUT PUT:
# count 2
# count 3
# count 4
# count 3
# count 2
# """


# class RefenceCountTest():
#     def __init__(self):
#         print('create object')

#     def __del__(self):
#         print(f'destroy {id(self)}')


# a = RefenceCountTest()
# a = 0
# print('end .....')

# print('='*30)

# class RefenceCountTest():
#     def __init__(self):
#         print('create object')
#         self.me = self

#     def __del__(self):
#         print(f'destroy {id(self)}')


# a = RefenceCountTest()
# a = 0
# print('end .....')

# print('='*30)

# import gc
# print(gc.get_count())
# print(gc.get_threshold())

import gc
import sys

l = []
print(sys.getrefcount(l))
l.append(l)
print(sys.getrefcount(l))
del l
print(sys.getrefcount(l))
