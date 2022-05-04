print('--- 퀵 정렬 ---')

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 원소가 1개면 종료
    if start >= end:
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 수 찾을 때까지
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 수 찾을 때까지
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 작은 수와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 작은 수와 큰 수 교체
            array[left], array[right] = array[right], array[left]
    # 분할 후 왼쪽과 오른쪽 각각 정렬 
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

'''
[실행결과]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

print('--- 퀵 정렬2 ---')

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼족
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

'''
[실행결과]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

print('--- 계수 정렬 ---')

array = [5, 4, 6, 5, 1, 2, 0, 9, 8, 5, 1, 0]
# 리스트 선언 및 전부 0으로 초기화
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): 
    for j in range(count[i]):
        print(i, end=' ')

'''
[실행결과]
0 0 1 1 2 4 5 5 5 6 8 9 
'''