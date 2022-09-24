# p118
# 실전문제 - 게임 개발

n, m = map(int, input().split())
x, y, direction = map(int, input().split()) # 북0 동1 남2 서3
d = [[0] * m for _ in range(n)]
d[x][y] = 1

map_info = []
for i in range(n):
    map_info.append(list(map(int, input().split()))) # 육지0 바다1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    
block = 1
turn_times = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 정면에 가보지 않은 칸
    if d[nx][ny] == 0 and map_info[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        block += 1
        continue
    # 회전 후 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_times += 1
    # 네 방향 모두 못가는 경우
    if turn_times == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if map_info[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_times = 0
        
    
print(block)