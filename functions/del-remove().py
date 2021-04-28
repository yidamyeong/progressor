# del 리스트명[인덱스번호] : 해당 인덱스 데이터 삭제
a = [1, 2, 3, 4, 5, 6, 7]
del a[1]
print(a)  # [1, 3, 4, 5, 6, 7]

del a[5]  # [1, 3, 4, 5, 6]
print(a)

# del a[5]  # 존재하지 않은 인덱스 번호 입력시 에러
# print(a)  # IndexError: list assignment index out of range

# 리스트명.remove(찾을 아이템)
a = [1, 2, 3, 4, 5, 6, 7]
a.remove(3)
print(a)  # [1, 2, 4, 5, 6, 7]

a.remove(8)  # 리스트에 없는 원소 입력시
print(a)  # ValueError: list.remove(x): x not in list
