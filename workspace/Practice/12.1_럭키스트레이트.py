score = input()
length = len(score)
sum1 = 0
sum2 = 0

for i in range(length // 2):
    sum1 += int(score[i])
    
for i in range(length // 2, length):
    sum2 += int(score[i])
    
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")