from collections import deque

gears = []
for _ in range(4):
  gears.append(deque((map(int, input()))))

# left[2] <-> right[6]
# 모든 톱니바퀴의 맞닿은 톱니의 상태를 모아서 회전시키는지 아닌지 정한다.
# 같은 값이면 회전X


def chainAct(n, d):  #n:돌리려는 태엽 d:1시계 -1반시계
  n -= 1
  temp = d
  isMove = [0] * 4
  isMove[n] = d
  if n != 4:  #우측 돌리기
    for i in range(n, 3):
      if gears[i][2] == gears[i + 1][6]:
        break
      else:
        d = -1 * d
        isMove[i + 1] = d
  d = temp
  if n != 0:  #좌측 돌리기
    for i in range(n, 0, -1):
      if gears[i][6] == gears[i - 1][2]:
        break
      else:
        d = -1 * d
        isMove[i - 1] = d

  for i in range(4):
    if isMove[i] != 0:
      gears[i].rotate(isMove[i])
  return


k = int(input())
for _ in range(k):
  num, dir = map(int, input().split())
  chainAct(num, dir)
result = 0

for i in range(4):
  result += (2**i) * gears[i][0]

print(result)
