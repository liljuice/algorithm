from collections import deque

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def dfs(graph, x, y):
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0

  while queue:
    ix, iy = queue.popleft()
    for i in range(8):
      nx = ix + dx[i]
      ny = iy + dy[i]
      if nx >= 0 and nx < h and ny >= 0 and ny < w:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 0
          queue.append((nx, ny))

  return


while True:
  count = 0
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  land = []
  for i in range(h):
    land.append(list(map(int, input().split())))
  #land[h][w]

  for i in range(h):
    for j in range(w):
      if land[i][j] == 1:
        dfs(land, i, j)
        count += 1

  print(count)
