from collections import deque

m, n = map(int, input().split())

box = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
  box.append(list(map(int, input().split())))


def bfs():
  queue = deque()
  for i in range(n):
    for j in range(m):
      if box[i][j] == 1:
        queue.append((i, j))

  while queue:
    ix, iy = queue.popleft()

    for i in range(4):
      nx = ix + dx[i]
      ny = iy + dy[i]

      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if box[nx][ny] == 0:
          box[nx][ny] = box[ix][iy] + 1
          queue.append((nx, ny))
  return


bfs()

res = 0
for i in box:
  for j in i:
    if j == 0:
      print(-1)
      exit()
  res = max(res, max(i))
print(res - 1)
