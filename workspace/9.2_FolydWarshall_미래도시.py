# 전체 회사 개수, 경로 개수 입력
n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for i in range(n + 1)]

# 리스트 무한으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
     
# 연결된 회사 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
# x번 회사, k번 회사 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

route = graph[1][k] + graph[k][x]
            
# 출력
if route >= INF:
    print("-1")
else:
    print(route)

