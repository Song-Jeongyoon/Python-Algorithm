n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # graph 밖을 벗어나면 강제 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 차례대로 노드 방문
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x, y + 1) 
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    return False
    
# 음료수 채우기
icecream = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            icecream += 1
print(icecream)


