# slice() 함수가 따로 있는건 아니고
array = ['a', 'b', 'c', 'd']
print(array[0:1])  # ['a']
print(array[1:3])  # ['b', 'c']

# del 기능을 활용해 slice 로 리스트 수정하기
# del list[:5]   처음부터 5번째 전까지 삭제
numbers = list(range(10))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del numbers[:5]
print(numbers)  # [5, 6, 7, 8, 9]

# 수정하기
numbers[1:3] = [66, 77]
print(numbers)  # [5, 66, 77, 8, 9]
