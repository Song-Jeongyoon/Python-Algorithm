# 예제 4-2 시각

n = int(input())
count = 0

for hour in range(n + 1):
    for minuite in range(60):
        for second in range(60):
            # 매 시각을 문자열로 바꿔 3이 있는지 확인
            if '3' in str(hour) + str(minuite) + str(second):
                count += 1

print(count)