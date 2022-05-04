'''
[예시답안]
'''
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게 담을 리스트
array = [0] * 11

# 각 무게에 해당하는 볼링공 개수 
for x in data:
    array[x] += 1
    
count = 0
for i in range(1, m + 1):
    # 무게가 i인 볼링공 개수 제외
    n -= array[i]
    # b가 선택하는 경우의 수와 곱하기
    count += array[i] * n
    
print(count)