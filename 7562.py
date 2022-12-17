from collections import deque

t = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


def bfs(x, y, destX, destY, mapSize):
  if x == destX and y == destY:
    return 0

  queue = deque()
  queue.append((x, y))
  chessMap = [[0] * mapSize for _ in range(mapSize)]

  while queue:
    ix, iy = queue.popleft()
    for i in range(8):
      nx = ix + dx[i]
      ny = iy + dy[i]

      if nx >= 0 and nx < mapSize and ny >= 0 and ny < mapSize:
        if chessMap[nx][ny] == 0:
          queue.append((nx, ny))
          chessMap[nx][ny] = chessMap[ix][iy] + 1
  return chessMap[destX][destY]


for _ in range(t):
  l = int(input())
  kX, kY = map(int, input().split())
  destX, destY = map(int, input().split())

  steps = bfs(kX, kY, destX, destY, l)
  print(steps)
