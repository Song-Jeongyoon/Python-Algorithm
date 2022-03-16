print("--- 재귀함수 종료 예제 ---")
# 스택구조와 동일
def recursive_function(i):
    if i == 10:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀함수를 종료합니다.")
    
recursive_function(1)

'''
[실행결과]
1 번째 재귀함수에서 2 번째 재귀함수를 호출합니다.
2 번째 재귀함수에서 3 번째 재귀함수를 호출합니다.
3 번째 재귀함수에서 4 번째 재귀함수를 호출합니다.
4 번째 재귀함수에서 5 번째 재귀함수를 호출합니다.
5 번째 재귀함수에서 6 번째 재귀함수를 호출합니다.
6 번째 재귀함수에서 7 번째 재귀함수를 호출합니다.
7 번째 재귀함수에서 8 번째 재귀함수를 호출합니다.
8 번째 재귀함수에서 9 번째 재귀함수를 호출합니다.
9 번째 재귀함수에서 10 번째 재귀함수를 호출합니다.
9 번째 재귀함수를 종료합니다.
8 번째 재귀함수를 종료합니다.
7 번째 재귀함수를 종료합니다.
6 번째 재귀함수를 종료합니다.
5 번째 재귀함수를 종료합니다.
4 번째 재귀함수를 종료합니다.
3 번째 재귀함수를 종료합니다.
2 번째 재귀함수를 종료합니다.
1 번째 재귀함수를 종료합니다.
'''

print("--- 팩토리얼 예제 ---")
# 첫번째 방법. 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 두번째 방법. 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    print(n, "*", factorial_recursive(n-1))
    return n * factorial_recursive(n-1) # n! = n * (n-1)

print("factorial_iterative :", factorial_iterative(5))
print("factorial_recursive :", factorial_recursive(5))

'''
[실행결과]
factorial_iterative : 120
2 * 1
3 * 2
2 * 1
4 * 6
2 * 1
3 * 2
2 * 1
5 * 24
2 * 1
3 * 2
2 * 1
4 * 6
2 * 1
3 * 2
2 * 1
factorial_recursive : 120
'''










