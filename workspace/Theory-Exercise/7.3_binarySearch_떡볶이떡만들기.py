n, m = list(map(int, input().split(' ')))
ricecakes = list(map(int, input().split()))

# 시작점, 끝점
start = 0
end = max(ricecakes)

result = 0
while(start <= end):
    total = 0 # 자른 떡의 길이 총합
    mid = (start + end) // 2
    
    for x in ricecakes:
        # 자른 떡의 길이 합 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기
    else:
        result = mid # 최대한 덜 잘랐을 때가 result
        start = mid + 1

print(result)


