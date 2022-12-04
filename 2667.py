from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
apart = []
n = int(input())


def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  apart[x][y] = 0
  count = 1

  while queue:
    ix, iy = queue.popleft()
    for i in range(4):
      nx = ix + dx[i]
      ny = iy + dy[i]

      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if apart[nx][ny] == 1:
          apart[nx][ny] = 0
          queue.append((nx, ny))
          count += 1

  return count


for _ in range(n):
  apart.append(list(map(int, input())))

result = []

for i in range(n):
  for j in range(n):
    if apart[i][j] == 1:
      result.append(bfs(i, j))

result.sort()
print(len(result))
for res in result:
  print(res)
