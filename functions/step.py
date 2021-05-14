# step 기능
# slice 한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
# list[시작값:끝값:step]
list1 = list(range(10))
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[5:10:2])  # [5, 7, 9]
print(list1[0:10:4])  # [0, 4, 8]

