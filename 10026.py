from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
grid = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
  grid.append(list(input()))


def bfs(a, b, color):
  queue = deque()
  queue.append((a, b))
  visited[a][b] = True

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if visited[nx][ny] == False and grid[nx][ny] == color:
          queue.append((nx, ny))
          visited[nx][ny] = True

  return


count = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(i, j, grid[i][j])
      count += 1

for i in range(n):
  for j in range(n):
    if grid[i][j] == 'R':
      grid[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

countRG = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(i, j, grid[i][j])
      countRG += 1

print(count, countRG)
