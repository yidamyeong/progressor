#  스택 구현시 유용한 append - pop

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
print(stack)
stack.pop()  # 최상단 원소 제거
print(stack)
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 스택 최상단 원소부터 (나중에 들어온 것부터) 출력
print(stack)  # 최하단 원소부터 출력
