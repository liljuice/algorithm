n, m, b = map(int, input().split())
land = []
res = []
for _ in range(n):
  land.append(list(map(int, input().split())))

for height in range(0, 257):
  time = 0
  inven = b
  for i in range(n):
    for j in range(m):
      gap = land[i][j] - height
      if gap > 0:  #더 높다면 (양수)
        inven += gap
        time += gap * 2
      elif gap < 0:  #더 낮다면 (음수)
        inven += gap
        time -= gap
  if inven >= 0:
    res.append((height, time))

res.sort(key=lambda x: (x[1], -x[0]))

print(res[0][1], res[0][0])
"""
1. 높이 0~256 전부 확인 (브루트포스, 반복값이 적음)
2. 그 높이 기준으로, 더 높은 블록에서 캐고, 더 낮은 블록에 넣어서 가능한지 판단.
3. 가장 높은 것 출력
"""
