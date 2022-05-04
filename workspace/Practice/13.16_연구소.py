n, m = map(int(input().split()))
before = []
after = [[0] * m for _ in range(n)]
for _ in range(n):
    before.append(list(map(int(input().split()))))

# 동남서북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
  
# 바이러스가 사방으로 퍼지도록 - dfs
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < y:
            if after[nx][ny] == 0:
                after[nx][ny] = 2
                virus(nx, ny)
                
# 안전 영역 계산
def safeArea():
    safeArea = 0
    for i in range(n):
        for j in range(m):
            if after[i][j] == 0:
                safeArea += 1

# 울타리를 설치하며 안전 영역 계산 - dfs 
def dfs(hence):
    global result
    if hence == 3:
        for i in range(n):
            for j in range(m):
                after[i][j] = before[i][j]
        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if after[i][j] == 2:
                    virus(i, j)
        # 최대 안전 영역 계산
        result = max(result, safeArea())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for i in range(m):
            if before[i][j] == 0:
                before[i][j] = 1
                hence += 1
                dfs(hence)
                before[i][j] = 0
                hence -= 1
                
dfs(0)
print(result)
                
        