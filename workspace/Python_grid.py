"""
[문제1] 거스름론
당신은 음식점의 계산을 도와주는 점원이다.
카운터에는 거스름돈으로 사용할 500원, 100운, 50원, 10원짜리 동전이 무수히 존재한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""


n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)

"""
[문제2] 큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수를 만든다.
배열의 특정 인텍스에 해당하는 수는 연속 k번을 초과하여 더해질 수 없고,
서로 다른 인덱스에 해당하는 수가 같은 경우에는 서로 다른 것으로 간주한다.
"""

#1
# n, m, k 입력
n, m, k = map(int, input().split())
# n개의 자연수 입력
num = list(map(int, input().split()))

# num에서 가장 큰 수와 두번째로 큰 수
num.sort()
first = num[n-1]
second = num[n-2]

result = 0

while True:
    for i in range(k):
        if m==0:
            break
        result += first
        m -= 1
    if m==0:
        break
    result += second
    m -= 1

print(result)


#2
# n, m, k 입력
n, m, k = map(int, input().split())
# n개의 자연수 입력
num =  list(map(int, input().split()))

# 가장 큰 수와 두번째로 큰 수
num.sort()
first = num[n-1]
second = num[n-2]

# 가장 큰 수가 다 합해진 수
countF = int(m/(k+1)*k*first + m%(k+1)*first)
# 두번째로 큰 수가 다 합해진 수
countS = int(m/(k+1)*second)

result = countF + countS
print(result)


"""
[문제3] 숫자 카드 게임
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는다
1. 숫자가 쓰인 카드들이 N X M 형태로 놓여있다. (N은 행, M은 열)
2. 먼저 뽑고자 하는 카드가 포합되어 있는 행을 선택한다
3. 그다음 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드를 뽑아야 한다
"""

# n, m 입력
n, m = map(int, input().split())

minList = []
result = 0

# 한 줄씩 입력
for m in range(n):
    num = list(map(int, input().split()))
    minList.append(min(num))

result = max(minList)
print(result)


'''
# 예시답안
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
'''

"""
[문제4] 1이 될 떄까지
어떤 수 N이 1이 될 때까지의 과정을 다음 두개 중 하나를 반복적으로 선택하여 수행하려 한다.
1. N에서 1을 뺀다
2. N을 K로 나눈다.
N과 K가 주어질 떄 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행하는 최소 횟수를 구하는 프로그램을 작성하시오.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
"""

n, k = map(int, input().split())

result = 0

while True:
    # target = N을 K의 배수로 만듦
    target = (n // k) * k
    n = target
    # N이 K의 배수가 될 때까지 1씩 제거
    result += (n - target)
    
    # N이 K보다 작다면 (더 나눌 수 없으면)
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

# 박지수님 풀이
N, K = map(int, input().split())
count = 0
while True:
    if N == 1:
        break
    if N % K != 0:
        N -= 1
    count += 1
    if N % K == 0:
        N /= K
        count += 1
print(count)







