# 대입식을 사용해 컴프리헨션 안에서 반복작업을 피하라

stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

# 각 부품의 몇 세트 분량의 재고가 있는지 알고 싶음.
order = ['screws', 'wingnuts', 'clips']

BATCH_SIZE = 8  # 부품을 8개씩 써야 함


def get_batches(count, size):
    return count // size
    # screws 의 경우 35개 있으니 4세트


result = {}

for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)

found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}

print(found)

# 대입식(왈러스 연산자)를 사용

found_2 = {name: batches for name in order
           if (batches := get_batches(stock.get(name, 0), 8))}

print(found_2)
