from collections import deque

m, n, h = map(int, input().split())
box = []
first_tomato = []
#box[i][j][k] i층 j행 k열
for i in range(h):
  temp = []
  for j in range(n):
    temp.append(list(map(int, input().split())))
    for k in range(m):
      if temp[j][k] == 1:
        first_tomato.append((i, j, k))
  box.append(temp)

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]


def bfs():
  queue = deque()
  for f in first_tomato:
    queue.append(f)

  while queue:
    z, x, y = queue.popleft()
    for i in range(6):
      iz = z + dz[i]
      ix = x + dx[i]
      iy = y + dy[i]

      if iz < 0 or iz >= h or ix < 0 or ix >= n or iy < 0 or iy >= m:
        continue
      if box[iz][ix][iy] == 0:
        box[iz][ix][iy] = box[z][x][y] + 1
        queue.append((iz, ix, iy))
  return


bfs()
zero = int(1e9)
temp = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if box[i][j][k] == 0:
        temp = zero
      elif box[i][j][k] > temp:
        temp = box[i][j][k]

if temp == zero:
  print(-1)
else:
  print(temp - 1)
