a = ['a', 'b', 47, 11, 22, 14, 'h']
b = a[:]    # list a 를 복사한 새 리스트를 얻는다.

print(a)
print(b)
print(id(a))
print(id(b))
print(b == a)
print(b is a)


a = ['a', 'b', 47, 11, 22, 14, 'h']
b = a
print(f'이전 a: {a}')
print(f'이전 b : {b}')
print(id(a))
print(id(b))

a[:] = [101, 102, 103]
print(a is b)
print(a == b)
print(id(a))
print(id(b))
print(f'이후 a : {a}')
print(f'이후 b : {b}')
