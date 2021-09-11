
# 제어 하위 식이 세개 이상인 컴프리헨션은 이해하기 어려우므로 피해야한다.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]

print(flat)

flat_list = []
for row in matrix:
    for x in row:
        flat_list.append(x)

print(flat_list)


# 제어 하위식 세개 이상인 경우

my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [1, 2, 3]],
    [[4, 5, 6], [7, 8, 9]],
]

my_lists_flat = [x for sublist1 in my_lists
                 for sublist2 in sublist1
                 for x in sublist2]


print(my_lists_flat)

my_lists_flat_list = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        for x in sublist2:
            my_lists_flat_list.append(x)

print(my_lists_flat_list)
