from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0


def bfs(baechu, x, y):
  queue = deque()
  queue.append((x, y))
  baechu[x][y] = 0

  while queue:
    ix, iy = queue.popleft()

    for i in range(4):
      nx = ix + dx[i]
      ny = iy + dy[i]

      if nx >= 0 and nx < m and ny >= 0 and ny < n:
        if baechu[nx][ny] == 1:
          baechu[nx][ny] = 0
          queue.append((nx, ny))

  return


t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  baechu = [[0] * n for _ in range(m)]
  count = 0

  for i in range(k):
    x, y = map(int, input().split())
    baechu[x][y] = 1

  for i in range(m):
    for j in range(n):
      if baechu[i][j] == 1:
        bfs(baechu, i, j)
        count += 1

  print(count)
