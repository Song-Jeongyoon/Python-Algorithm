'''
[예시답안]
'''
data = input()
count0 = 0 # 전부 0으로 바꾸기
count1 = 1 # 전부 1로 바꾸기

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 확인    
for i in range(1, len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '0':
            count1 += 1
        else:
            count0 += 1
        
print(min(count0, count1))            

