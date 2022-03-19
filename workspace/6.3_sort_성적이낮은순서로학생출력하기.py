n = int(input())

stu = []
for i in range(n):
    stu_data = input().split()
    stu.append((stu_data[0], int(stu_data[1])))
    
# 점수를 기준으로 정렬 (key 활용)
stu = sorted(stu, key=lambda score: score[1])

# 정렬이 수행된 결과를 출력
for name in stu:
    print(name[0], end=' ')


