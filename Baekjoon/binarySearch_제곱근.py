#13706번
"""
문제
정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 양의 정수 N이 주어진다. 정수 N의 제곱근은 항상 정수이며, N의 길이는 800자리를 넘지 않는다.

출력
첫째 줄에 정수 N의 제곱근을 출력한다.
"""

n = int(input())
start = 1
end = n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        end = mid - 1   
    else:
        start = mid + 1

