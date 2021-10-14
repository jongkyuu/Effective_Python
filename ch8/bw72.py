from bisect import bisect_left
import random
import timeit

size = 10 ** 5
iterations = 1000

data = list(range(size))
to_lookup = [random.randint(0, size)
             for _ in range(iterations)]

def run_linear(data, to_lookup):
    for index in to_lookup:
        data.index(index)

def run_bisect(data, to_lookup):
    for index in to_lookup:
        bisect_left(data, index)

baseline = timeit.timeit(
    stmt='run_linear(data, to_lookup)',
    globals=globals(),
    number=10)
print(f'선형 검색: {baseline:.6f}초')

comparison = timeit.timeit(
    stmt='run_bisect(data, to_lookup)',
    globals=globals(),
    number=10)
print(f'이진 검색: {comparison:.6f}초')

# slowdown = 1 + ((baseline - comparison) / comparison)
# print(f'선형 검색이 {slowdown:.1f}배 더 걸림')