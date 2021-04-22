# n, k 입력받기
n, k = map(int, input().split())
print(n, k)

# 배열 A 원소 입력받기
a = list(map(int, input().split()))
print(a)

# 배열 B 원소 입력받기
b = list(map(int, input().split()))
print(b)

# a 에서 가장 작은 값을 b에서 가장 큰 값과 교환해야 함
a.sort()
b.sort(reverse=True)

print('a 오름차순:', a)
print('b 내림차순:', b)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print('a:', a)
print('b:', b)
print(sum(a))  # 배열 a 모든 원소 합 출력

