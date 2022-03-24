n = int(input())
n_list = list(map(int, input().split()))
n_list.sort() # 이진탐색은 배열 내부의 데이터가 정렬되어 있어야 사용가능

m = int(input())
m_list = list(map(int, input().split()))
m_list.sort()

def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None
            
for i in m_list:
    result = search(n_list, i, 0, n - 1)  
    if result == None:
        print("no", end =' ')
    else:
        print("yes", end = ' ')         
        
        