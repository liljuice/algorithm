n, m = map(int, input().split())
loc = list(map(int, input().split()))
neg = []
pos = []
move = []  #움직일 거리

for l in loc:
  if l < 0:
    neg.append(l)
  else:
    pos.append(l)

neg.sort()
pos.sort(reverse=True)

for i in range(0, len(neg), m):
  move.append(abs(neg[i]))

for i in range(0, len(pos), m):
  move.append(pos[i])

move.sort(reverse=True)
ans = 0

ans += move[0]
for i in range(1,len(move)):
  ans += move[i] * 2

print(ans)
  
"""
-39 -37 -29 -28 -6 2 11
ㅇ       ㅇ      ㅇ
-39 -29 -6 11
가장 먼 책 + 그 방향의 책부터 집어버리자.
마지막에 돌아올 필요 없는 건 가장 먼 책으로.
39 + 29*2 + 6*2 + 11*2

-45 -26 -18 -9 -4 22 40 50
50 + 45*2 + 9*2
"""
