address = 'Four score and seven years ago...'

# 공백을 찾아 index를 반환해주는 함수


def index_words_iter(text):
    if text:
        yield 0
    for idx, letter in enumerate(text):
        if letter == ' ':
            yield idx + 1


it = index_words_iter(address)
print(next(it))
print(next(it))
print(list(it))  # 이터레이터에 상태가 있으므로 주의! 재사용 불가.


# 리스트로 쉽게 변환 가능
result_list = list(index_words_iter(address))
print(result_list)
