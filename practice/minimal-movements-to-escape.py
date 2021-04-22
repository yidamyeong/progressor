from collections import deque

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if n <= nx < 0 or m <= ny < 0:
                continue
            # 벽인 경우 무시
            if nodes[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if nodes[nx][ny] == 1:
                nodes[nx][ny] = nodes[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return nodes[n - 1][m - 1]


# N, M 입력 받기
n, m = map(int, input().split())

# 미로의 노드값 입력받기 (2차원 리스트의 맵 정보 입력)
nodes = []
for _ in range(n):
    nodes.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 를 수행한 결과 출력
print(bfs(0, 0))
