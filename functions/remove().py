# 리스트명.remove(찾을 아이템)
a = [1, 2, 3, 4, 5, 6, 7]
a.remove(3)
print(a)  # [1, 2, 4, 5, 6, 7]

a.remove(8)  # 리스트에 없는 원소 입력시
print(a)  # ValueError: list.remove(x): x not in list


