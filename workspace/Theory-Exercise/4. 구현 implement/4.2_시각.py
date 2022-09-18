# page 113
# 예제 4-2 시각

n = int(input())
count = 0

for hour in range(n + 1):
    for minuite in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minuite) + str(second):
                count += 1
                
print(count)

