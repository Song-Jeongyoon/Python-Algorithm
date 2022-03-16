print('--- 인접 리스트 방식 예제 ---')
# 행이 4개인 2차원 리스트로 표현
graph = [[] for _ in range(4)]

#(노드, 간선)
graph[0].append((1, 7))
graph[0].append((2, 5))
graph[0].append((3, 9))
graph[1].append((0, 7))
graph[2].append((0, 5))
graph[3].append((0, 9))

print(graph)

'''
[실행결과]
[[(1, 7), (2, 5), (3, 9)], [(0, 7)], [(0, 5)], [(0, 9)]]
'''

print('--- DFS 예제 ---')
def dfs(graph, v, visited):
    # 현재의 노드를 방문처리
    visited[v] = True
    print(v, end = ' ')
    # 현재의 노드와 연결된 다른 노드들을 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
# 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 6],
    [1, 4],
    [1, 5],
    [2, 6, 7],
    [3],
    [1, 4],
    [4]
]
    
# 각 노드가 방문한 정보를 1차원 리스트로 표현
visited = [False]*9

dfs(graph, 1, visited)

'''
[실행결과]
1 2 4 6 7 3 5 
'''

print('--- BFS 예제 ---')
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])
    # 현재의 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나를 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결되어 있지만 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 6],
    [1, 4],
    [1, 5],
    [2, 6, 7],
    [3],
    [1, 4],
    [4]
]
    
# 각 노드가 방문한 정보를 1차원 리스트로 표현
visited = [False]*9

bfs(graph, 1, visited)

'''
[실행결과]
1 2 3 6 4 5 7 
'''
