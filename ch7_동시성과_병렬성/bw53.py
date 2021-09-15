import select
from time import time


def slow_systemcall():
    select.select([], [], [], 0.1)


# 이 시스템 호출을 연속해서 실행하면 시간이 선형으로 증가

start = time()
for _ in range(5):
    slow_systemcall()
end = time()
print('Took %.3f seconds' % (end - start))
