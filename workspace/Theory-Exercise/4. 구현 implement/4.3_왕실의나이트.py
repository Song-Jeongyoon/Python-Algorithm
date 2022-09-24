# p115
# 실전문제 - 왕실의 나이트

start = input()
row = int(start[1])
col = int(ord(start[0])) - int(ord('a')) + 1

moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

count = 0
for move in moves:
    nrow = row + move[0]
    ncol = col = move[1]
    if nrow < 1 or nrow > 8 or ncol < 1 or ncol > 8:
        continue
    count += 1
    
print(count)