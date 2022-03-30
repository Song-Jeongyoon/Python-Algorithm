# 4158번
"""
문제
상근이와 선영이는 동시에 가지고 있는 CD를 팔려고 한다. CD를 몇 개나 팔 수 있을까?

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스의 첫째 줄에는 상근이가 가지고 있는 CD의 수 N, 선영이가 가지고 있는 CD의 수 M이 주어진다. N과 M은 최대 백만이다. 
다음 줄부터 N개 줄에는 상근이가 가지고 있는 CD의 번호가 오름차순으로 주어진다. 다음 M개 줄에는 선영이가 가지고 있는 CD의 번호가 오름차순으로 주어진다. 
CD의 번호는 십억을 넘지 않는 양의 정수이다. 입력의 마지막 줄에는 0 0이 주어진다.
상근이와 선영이가 같은 CD를 여러장 가지고 있는 경우는 없다.

출력
두 사람이 동시에 가지고 있는 CD의 개수를 출력한다.
"""

n, m = map(int, input().split())
nlist = []
mlist = []
for i in range(n):
    nlist.append(int(input()))
     
for i in range(m):
    mlist.append(int(input()))    

z1, z2 = map(int, input().split())

nstart = nlist[0]
nend = nlist[n - 1]

# 중복되는 값 찾기
for i in mlist:
    nmid = (nstart + nend) // 2
    if nmid == mlist[i]:
        print(nmid)
        break
    elif nmid > mlist[i]:
        nend = nmid - 1
    else:
        nstart = nmid + 1
        
        
'''
[지수님 답안 - 런타임에]
n, m = map(int, input().split())
n_list = []
m_list = []
for i in range(n):
  n_list.append(int(input()))
for i in range(m):
  m_list.append(int(input()))
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
count = 0

for item in n_list:
  start = 0
  end = len(m_list) - 1
  while start <= end:
    mid = (start + end) // 2
    if m_list[mid] == item:
      count += 1
      break
    elif m_list[mid] < item:
      start = mid + 1
    else:
      end = mid - 1

print(count)
'''