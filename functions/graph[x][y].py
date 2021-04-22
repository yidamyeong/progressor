n = int(input('리스트 원소 개수 입력 : '))

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # 여기서 입력받음 (n개 만큼)

print(graph)  # 2차원배열 형태 eg. [[1, 0, 2], [5], [6, 8]]

print(graph[1][1])
print(graph[0][2])
