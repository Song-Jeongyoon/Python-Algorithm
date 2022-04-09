s = input()
num = list(map(int, s))

result = max(num)
num.remove(max(num))
for i in num:
    if i == 0 or i == 1:
        # 더하기
        result += i
    else:
        # 곱하기
        result *= i
        
print(result)

