import time

n, k = map(int, input().split())
start_time = time.time()

count = 0

while True:
    if n % k == 0:
        n = n / k
        count += 1
    else:
        n = n - 1
        count += 1        
    if n == 1:
        break
    
print(count)

end_time = time.time()
print("time", end_time - start_time)