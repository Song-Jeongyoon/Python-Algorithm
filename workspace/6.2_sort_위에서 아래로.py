n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
    
numbers.sort(reverse=True)

for i in range(len(numbers)):
        print(numbers[i], end=' ')
