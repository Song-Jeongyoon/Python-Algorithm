"""
[문제 1-1] 상하좌우
"""
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

# 다른 풀이 ----------
n = int(input())
X, Y = 1, 1
moves = input().split()

for move in moves:
  if move == 'L':
    if X == 1:
      continue
    X -= 1
  if move == 'R':
    if X == n:
      continue
    X += 1
  if move == 'U':
    if Y == 1:
      continue
    Y -= 1
  if move == 'D':
    if Y == n:
      continue
    Y += 1

print(X, Y)
   

"""
[문제 1-2] 시각
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
"""
hour = int(input())
count = 0

for i in range(hour+1): # hour에 1을 더해주어야 hour만큼 반
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


"""
[문제2] 왕실의 나이트
"""
loc = input()
row = int(loc[1])
col = int(ord(loc[0])) - int(ord('a')) + 1

# 나이트의 이동 방향
steps = [(-2,-1), (-1, -2), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1),]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[0]
    
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <=8:
        result += 1
        
print(result)


"""
[문제3] 게임 개발
"""
# n, m 입력
n, m = map(int, input().split())

# 지나간 좌표는 1로 표시해주어야 하므로(조건2) 먼저 2중리스트 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 위치와 방향 입력
x, y, direction = map(int, input().split())   # 0-북, 1-동, 2-남, 3-서
# 현재 좌표 방문
d[x][y] = 1

# 맵 정보 입력
map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split()))) # 0-육지, 1-바다

# 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 좌회전
def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction == 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and map_list[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # 회전 후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
        
    # 네 방향 모두 막힌 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있는 경우
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0

print(count)


