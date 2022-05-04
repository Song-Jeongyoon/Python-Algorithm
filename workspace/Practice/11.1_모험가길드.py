# 오류 수정 중인 코드
n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
for i in data:
    group += 1
    data.remove(i)
    if i - 1 > len(data):
        break

print(group)

'''
[예시답안]
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data:
    count += 1
    if count >= i :
        group += 1
        count = 0
        
print(group)