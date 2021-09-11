import pickle


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper


@trace
def fibonacci(n):
    """Return n 번째 피보나치 수"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci(4)

print(fibonacci)
help(fibonacci)


# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# 데코레이터가 감싸고 있는 원래 함수의 위치를 찾을 수 없기 떄문에 객체 직렬화도 깨진다.

pickle.dumps(fibonacci)
