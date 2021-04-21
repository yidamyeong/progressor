# 큐 (Queue) 구현을 위해 deque 라이브러리 사용
from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 역순으로 바꾸기
print(queue)  # reverse() 후 나중에 들어온 원소부터 출력
print(queue[2])  # 이때는 slice 를 쓸 수 없다. -> islice 라는게 있긴 함 (검색 요)
