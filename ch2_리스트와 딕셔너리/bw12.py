# stride : 리스트[시작:끝:증가값] 형태로 일정한 간격을 두고 슬라이싱을 할 수 있는 구문
x = [1, 2, 3, 4, 5, 6]
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

# 바이트 문자열을 역으로 뒤집는 일반적인 기법
x = b'abcde'
y = x[::-1]
print(x)
print(y)

# 유니코드 문자열을 역으로 뒤집기
x = '寿司'
y = x[::-1]
print(x)
print(y)

# 유니코드 문자열을 UTF-8로 인코딩 했을때 역으로 뒤집기가 작동하지 않음
# 2바이트 이상으로 이뤄졌던 문자들은 utf-8 인코딩의 바이트 순서를 뒤집으면 코드가 깨지기 때문에, 이 바이트 문자열을 유니코드 문자열로 디코딩 할 수 없음.
x = '寿司'
x2 = x.encode('utf-8')
y = x2.decode('utf-8')
print(x2)
print(y)
y2 = x2[::-1]
print(y2)
# x3 = y2.decode('utf-8')   # 'utf-8' codec can't decode byte 0xb8 in position 0: invalid start byte
# print(x3)

# 아스키 코드에 해당하는 글자들은 1바이트 값으로 인코딩 되기 떄문에

# 음수 증가값 응용
x = [1, 2, 3, 4, 5, 6, 7, 8]
print(x[::2])
print(x[::-2])
print(x[2::2])
print(x[-2::-2])
print(x[-2:2:-2])
print(x[2:2:-2])

# 슬라이싱 구문에 스트라이딩까지 들어가면 혼란스럽기 때문에
# 증가값과 시작, 끝 슬라이싱 구문을 나눠서 사용하라
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = x[::2]
z = y[1:-1]

print(y)
print(z)
print(x[2:-1:2])
