from collections import deque 

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [0] * (n + 1) 
distance[x] = 0       

# bfs 함수
queue = deque([x])
while queue:
    now = queue.popleft()
    print('now =', now)
    for next_n in graph[now]:
        if distance[next_n] == 0:
            distance[next_n] = distance[now] + 1
            print('distance[next_n] =', distance[next_n])
            print('distance[now] =', distance[now])
            
            queue.append(next_n)
            print(queue)
            print(' ')
                

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# k가 없을 경우
if check == False:
    print("-1")


'''
[입력예시
4 4 2 1

1 2

1 3

2 3

2 4 에서 bfs 함수 진행과정은]

now = 1
distance[next_n] = 1
distance[now] = 0
deque([2])
 
distance[next_n] = 1
distance[now] = 0
deque([2, 3])
 
now = 2
distance[next_n] = 2
distance[now] = 1
deque([3, 4])
 
now = 3
now = 4

'''
