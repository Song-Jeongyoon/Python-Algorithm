import time
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()
data.sort(reverse=True)

result = 0

while True:
    for _ in range(k):
        result += data[0]
        m -= 1
        if m==0:
            break
    result += data[1]
    m -= 1
    if m==0:
        break

print(result)

end_time = time.time()
print("time", end_time - start_time)

'''
#[경민님 풀이]
import time

n, m, k = map(int, input().split()) 
nums = list(map(int, input().split()))

start_time = time.time()

result = 0
count = 0

nums.sort()

while count < m:
    result += nums[-1] * k 
    count+=k
    result += nums[-2] 
    count+=1

print(result)

end_time = time.time()
print("time", end_time - start_time)

'''