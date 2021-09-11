
# 리스트 컴프리헨션 (List Comprehension)
a = [1, 2, 3, 4, 5]
squares = [x**2 for x in a]
print(squares)

# lambda 사용
alt = map(lambda x: x**2, a)
print(list(alt))


# 리스트 컴프리핸션은 lambda식을 사용하지 않기 떄문에 map과 filter 내장함수를 사용하는 것보다 이해하기 쉽다.

# 리스트 컴프리핸션 사용
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
print(even_squares_dict)

# lambda식 사용
alt_dict = dict(map(lambda x: (x, x**2), filter(lambda x: x % 2 == 0, a)))
print(alt_dict)
