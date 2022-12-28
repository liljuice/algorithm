from collections import deque

n = int(input())
area = []
for _ in range(n):
  area.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, height, visited):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  while queue:
    nx, ny = queue.popleft()
    for i in range(4):
      ix = nx + dx[i]
      iy = ny + dy[i]
      if ix < 0 or ix >= n or iy < 0 or iy >= n:
        continue
      if area[ix][iy] > height and not visited[ix][iy]:
        queue.append((ix, iy))
        visited[ix][iy] = True
        
  return



safe = []

for h in range(100):
  visited = [[False] * n for _ in range(n)]
  temp = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j] and area[i][j] > h:
        bfs(i,j,h,visited)
        temp += 1
  safe.append(temp)

print(max(safe))
