# 10162번 전자레인지
# A-5분, B-1분, C-10초
# ABC를 최소회수로 눌러서 T초가 되도록
# 세 버튼으로 T를 맞출 수 없으면 -1 출력

t = int(input())
acount = 0
bcount = 0
ccount = 0

if t % 10 == 0:
    for i in range(t):
        if t >= 300:
            t -= 300
            acount +=1
        if t >= 60:
            t -= 60
            bcount +=1
        if t < 60:
            t -= 10
            ccount += 1
        if t == 0:
            break
    print(acount, bcount, ccount)   
                    
else:
    print(-1)

    

