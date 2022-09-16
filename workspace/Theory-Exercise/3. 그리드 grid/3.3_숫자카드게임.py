import time

n, m = map(int, input().split())
start_time = time.time()

data = []
mindata = []
for m in range(n):
    data = list(map(int, input().split()))
    mindata.append(min(data))
    
print(max(mindata))

end_time = time.time()
print("time", end_time - start_time)    
    
