# -*- coding: utf-8 -*-
def outer_func():  # 1
    message = 'Hi'  # 3

    def inner_func():  # 4
        print(message)  # 6

    return inner_func  # 5


my_func = outer_func()  # 2
my_func()

print(my_func)  # 7
print()
print(dir(my_func))  # 8
print()
print(type(my_func.__closure__))  # 9
print()
print(my_func.__closure__)  # 10
print()
print(my_func.__closure__[0])  # 11
print()
print(dir(my_func.__closure__[0]))  # 12
print()
print(my_func.__closure__[0].cell_contents)  # 13

print('='*30)


def outer_func(tag):
    tag = tag

    def inner_func(txt):
        text = txt
        
        print('<{0}>{1}<{0}>'.format(tag, text))

    return inner_func


h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func('inner of h1 tag')
p_func('inner p tag')

