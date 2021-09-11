car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages)
print(car_ages_descending)

oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

# 시각적 잡음과 off-by-one error의 위험을 제거하기 위해 별표 식(starred expression)을 사용
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)


# 별표 식만 사용해 언패킹 할 수는 없다
# *others = car_ages_descending

# 한 수준의 언패킹 패턴에 별표 식을 두개 이상 쓸 수 없다.
# first, *middle, *second_middle, last = [1, 2, 3, 4]

# 권고하지는 않지만 다음 방식을 이해하면 별표 식을 언패킹 대입에 사용하는 방식에 대한 직관을 키울 수 있다.
car_inventory = {
    '시내': ('그랜저', '아반테', '티코'),
    '공항': ('제네시스 쿠페', '소나타', 'K5', '악센트'),
}

((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()
print(f'{loc1} 최고는 {best1}, 나머지는 {len(rest1)} 종')
print(f'{loc2} 최고는 {best2}, 나머지는 {len(rest2)} 종')


# 별표 식을 사용하면 언패킹할 이터레이터의 값을 깔끔하게 가져올 수 있다.
def generate_csv():
    yield ('날짜', '제조사', '모델', '연식', '가격')
    for i in range(100):
        yield ('2019-03-25', '현대', '소나타', '2010', '2400만원')
        yield ('2019-03-26', '기아', '프라이드', '2008', '1400만원')


all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV 헤더:', header)
print('행 수: ', len(rows))

# 별표 식으로 언패킹하면 이터레이터가 내보내는 ㅐㄴ용 중에 첫번째(헤더)와 나머지를 쉽게 나눠서 처리할 수 있다.
it = generate_csv()
header, *rows = it
print('CSV 헤더:', header)
print('행 수: ', len(rows))
