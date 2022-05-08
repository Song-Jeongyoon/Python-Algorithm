from collections import deque

n, k = map(int, input().split())

graph = [] # 보드
virus = [] # 바이러스
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if [i][j] != 0:
            # 바이러스 종류, 시간, x, y
            virus.append(graph[i][j], 0, i, j)
    
target_s, target_x, target_y = map(int, input().split())

virus.sort()
q = deque(virus)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
while q:
    virus, s, x, y = q.popleft()
    if target_s == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 아직 방문하지 않은 곳에 바이러스 넣기
        if 0 <= nx and 0 <= ny and n > nx and n > ny:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, x, y))

print(graph[target_x - 1][target_y - 1])
