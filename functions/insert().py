# insert : 리스트명.insert(입력할 index, 값)
a = [22, 23, 24, 25]
a.insert(2, 88)
print(a)  # [22, 23, 88, 24, 25] .. 1번 인덱스와 2번 인덱스 사이에 새로운 값이 들어간다. 즉 88이 인덱스 2가 된다.

b = ['서울', '광주', '부산']
b.insert(3, '대전')
print(b)  # ['서울', '광주', '부산', '대전']

b.insert(3, '강원')
print(b)  # ['서울', '광주', '부산', '강원', '대전']
