import sys
input = sys.stdin.readline
INF = int(1e9) # 10억으로 무한을 의미

# 노드와 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for i in range(n + 1)]
# 방문 여부
visited = [False] * (n + 1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)


# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b로가는 비용이 c
    graph[a].append((b, c))
    
# 미방문 노드 중 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드 초기화
    distance[start] = 0
    visited[start] = True
    # 시작노드로부터 당장 도달이 가능한 노드를 먼저 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전채 n - 1개 노드 반복
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 타 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 타 노드로 이동하는게 더 짧은 경로일 때
            if cost < distance[j[0]]:
                distance[j[0]] = now
                
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


