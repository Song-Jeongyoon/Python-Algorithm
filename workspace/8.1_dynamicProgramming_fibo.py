# 메모이제이션 기법을 활용한 피보나치 수열 (재귀적) -----
d = [0] * 100 # 리스트 초기화

def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99)) # 218922995834555169026

# 호출되는 함수 확인
d = [0] * 100

def fibo2(x):
    print('f(' + str(x) + ')', end=' ')
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제
    d[x] = fibo2(x - 1) + fibo2(x - 2)
    return d[x]

fibo2(6) # f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) 


# 메모이제이션 기법을 활용한 피보나치 수열2 (반복문) -----
d = [0] * 100 

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i -2]
    
print(d[n]) # 218922995834555169026